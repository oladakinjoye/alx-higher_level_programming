#!/usr/bin/python3
for k in range(10):
    for j in range(k+1, 10):
        print(f"{k}{j}", end="")
        if k != 8 or j != 9:
            print(", ", end="")
        else:
            print()
