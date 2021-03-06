#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Enables callbacks into functions to be automatically invoked
when various events occur to the debuggee (e.g. STOP on SIGINT)
by using a decorator.
"""
import functools
import sys
import traceback

import gdb
import pwndbg.stdio

debug = False
pause = 0


# There is no GDB way to get a notification when the binary itself
# is loaded from disk, by the operating system, before absolutely
# anything happens
#
# However, we get an Objfile event when the binary is loaded, before
# its entry point is invoked.
#
# We also get an Objfile event when we load up GDB, so we need
# to detect when the binary is running or not.
class StartEvent(object):
    def __init__(self):
        self.registered = set()
        self.running    = False
    def connect(self, function):
        self.registered.add(function)
    def disconnect(self, function):
        if function in self.registered:
            self.registered.remove(function)
    def on_new_objfile(self):
        if self.running or not gdb.selected_thread():
            return

        self.running = True

        for function in self.registered:
            function()

    def on_stop(self):
        self.running = False

gdb.events.start = StartEvent()

# In order to support reloading, we must be able to re-fire
# all 'objfile' and 'stop' events.
registered = {gdb.events.exited: [],
              gdb.events.cont: [],
              gdb.events.new_objfile: [],
              gdb.events.stop: [],
              gdb.events.start: []}

class Pause(object):
    def __enter__(self, *a, **kw):
        global pause
        pause += 1
    def __exit__(self, *a, **kw):
        global pause
        pause -= 1

def connect(func, event_handler, name=''):
    if debug:
        print("Connecting", func.__name__, event_handler)

    @functools.wraps(func)
    def caller(*a):
        if debug: sys.stdout.write('%r %s.%s %r\n' % (name, func.__module__, func.__name__, a))
        if pause: return
        with pwndbg.stdio.stdio:
            try:
                func()
            except Exception as e:
                traceback.print_exc()
                raise e

    registered[event_handler].append(caller)
    event_handler.connect(caller)
    return func

def exit(func):        return connect(func, gdb.events.exited, 'exit')
def cont(func):        return connect(func, gdb.events.cont, 'cont')
def new_objfile(func): return connect(func, gdb.events.new_objfile, 'obj')
def stop(func):        return connect(func, gdb.events.stop, 'stop')
def start(func):       return connect(func, gdb.events.start, 'start')

def after_reload():
    return
    # if gdb.selected_inferior().pid:
    #     for f in registered[gdb.events.new_objfile]:
    #         f()
    #     for f in registered[gdb.events.stop]:
    #         f()

def on_reload():
    for event, functions in registered.items():
        for function in functions:
            event.disconnect(function)
        registered[event] = []

@new_objfile
def _start_newobjfile():
    gdb.events.start.on_new_objfile()

@stop
def _start_stop():
    gdb.events.start.on_stop()
