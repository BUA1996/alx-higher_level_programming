#!/usr/bin/python3
num = 0
for alpha in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alpha - num)), end="")
    if num == 0:
        num = 32
    else:
        num = 0
