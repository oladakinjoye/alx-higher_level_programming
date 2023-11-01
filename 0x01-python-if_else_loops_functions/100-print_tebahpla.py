#!/usr/bin/python3
output = ""

for i in range(25, -1, -1):
    if i % 2 == 0:
        output += chr(i + 97)
    else:
        output += chr(i + 65)

print(output, end="")
