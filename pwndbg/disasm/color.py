#!/usr/bin/env python
# -*- coding: utf-8 -*-
import capstone
import pwndbg.chain
import pwndbg.color
import pwndbg.disasm.jump

capstone_branch_groups = [
capstone.arm.ARM_GRP_CALL,
capstone.arm.ARM_GRP_JUMP,
capstone.arm64.ARM64_GRP_JUMP,
capstone.mips.MIPS_GRP_JUMP,
capstone.ppc.PPC_GRP_JUMP,
capstone.sparc.SPARC_GRP_JUMP,
capstone.x86.X86_GRP_CALL,
capstone.x86.X86_GRP_JUMP,
]

def instruction(ins):
    asm = u'%-06s %s' % (ins.mnemonic, ins.op_str)

    branch = any(g in capstone_branch_groups for g in ins.groups)
    taken  = pwndbg.disasm.jump.is_jump_taken(ins)

    if branch:
        asm = pwndbg.color.bold(asm)

    if ins.target is not None:
        sym    = pwndbg.symbol.get(ins.target)
        target = pwndbg.color.get(ins.target)
        const  = ins.target_constant

        # If it's a constant expression, color it directly in the asm.
        if const:
            asm = asm.replace(hex(ins.target), target)

            if sym:
                asm = '%-36s <%s>' % (asm, sym)
        elif sym:
            asm = '%-36s <%s; %s>' % (asm, target, sym)
        else:
            asm = '%-36s <%s>' % (asm, target)

    if taken:
        asm = pwndbg.color.green(u'✔ ') + asm
    else:
        asm = '  ' + asm

    return asm
