#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helpers for finding address mappings which are used as
a stack.

Generally not needed, except under qemu-user and for when
binaries do things to remap the stack (e.g. pwnies' postit).
"""

import gdb
import pwndbg.events
import pwndbg.memoize
import pwndbg.memory

# Dictionary of stack ranges.
# Key is the gdb thread ptid
# Value is a pwndbg.memory.Page object
stacks = {}

# Whether the stack is protected by NX.
# This is updated automatically by is_executable.
nx     = False

def find(address):
    """
    Returns a pwndbg.memory.Page object which corresponds to the
    currently-loaded stack.
    """
    if not stacks:
        update()

    for stack in stacks:
        if address in stack:
            return stack

def find_upper_stack_boundary(addr, max_pages=1024):
    addr = pwndbg.memory.page_align(int(addr))
    try:
        for i in range(max_pages):
            data = pwndbg.memory.read(addr, 4)
            if b'\x7fELF' == pwndbg.memory.read(addr, 4):
                break
            addr += pwndbg.memory.PAGE_SIZE
    except gdb.MemoryError:
        pass
    return addr

@pwndbg.events.stop
@pwndbg.memoize.reset_on_stop
def update():
    """
    For each running thread, updates the known address range
    for its stack.
    """
    curr_thread = gdb.selected_thread()

    try:
        for thread in gdb.selected_inferior().threads():
            thread.switch()
            sp = pwndbg.regs.sp

            # If we don't already know about this thread, create
            # a new Page mapping for it.
            page = stacks.get(thread.ptid, None)
            if page is None:
                start = pwndbg.memory.find_lower_boundary(sp)
                stop  = find_upper_stack_boundary(sp)
                page  = pwndbg.memory.Page(start, stop-start, 6 if not is_executable() else 7, 0, '[stack]')
                stacks[thread.ptid] = page
                continue
            elif page.objfile is None:
                page.objfile = '[stack]'

            # If we *DO* already know about this thread, just
            # update the lower boundary.
            low = pwndbg.memory.find_lower_boundary(page.vaddr)
            if low != page.vaddr:
                page.memsz  += (page.vaddr - low)
                page.vaddr   = low
    finally:
        curr_thread.switch()


@pwndbg.memoize.reset_on_stop
def current():
    """
    Returns the bounds for the stack for the current thread.
    """
    return find(pwndbg.regs.sp)

@pwndbg.events.exit
def clear():
    """
    Clears everything we know about any stack memory ranges.

    Called when the target process exits.
    """
    stacks.clear()
    global nx
    nx = False

@pwndbg.events.stop
@pwndbg.memoize.reset_on_exit
def is_executable():
    global nx
    nx = False

    PT_GNU_STACK = 0x6474e551
    ehdr         = pwndbg.elf.exe()

    for phdr in pwndbg.elf.iter_phdrs(ehdr):
        p_type = int(phdr['p_type'])
        if p_type == PT_GNU_STACK:
            nx = True

    return not nx
