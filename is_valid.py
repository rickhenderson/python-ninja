"""
is_valid.py
A short program to compare different ways
of writting a comparison.
Uses the python disassembler.
Author: Rick Henderson
"""
import dis

def is_valid_v1():
    valid = True
    value = 10
    comp = 11
    if comp < -value and comp > value:
        valid = False

    return valid

def is_valid_v2():
    valid = False
    value = 10
    comp = 11
    if comp >= -value and comp <= value:
        valid = True

    return valid

dis.dis(is_valid_v1)
print("Version 2: Using >= instead of <")
dis.dis(is_valid_v2)
