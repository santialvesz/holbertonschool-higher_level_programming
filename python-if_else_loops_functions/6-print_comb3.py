#!/usr/bin/python3
for i in range(0, 9):
    for q in range(1, 10):
        if i < q:
            print("{:d}{:d}".format(i, q), end="")
            if i != 8:
                print(", ", end="")

print("")
