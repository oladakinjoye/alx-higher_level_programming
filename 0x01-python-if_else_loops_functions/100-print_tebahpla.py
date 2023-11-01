#!/usr/bin/python3
output = ""

for i in range(25, -1, -1):
    if i % 2 == 0:
        output += "{}{}".format(chr(i + 97), chr(i + 65))
    else:
        output += "{}{}".format(chr(i + 65), chr(i + 97))

print("{0}".format(output), end="")
