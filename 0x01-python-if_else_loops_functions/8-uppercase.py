#!/usr/bin/python3
def uppercase(s):
    for c in s:
        upper_char = chr(ord(c) - 32) if ord(c) >= ord('a') and ord(c) <= ord('z') else c
        print(upper_char, end="")
    print()
