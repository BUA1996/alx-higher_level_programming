#!/usr/bin/python3

def magic_calculation(a, b):
    last = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                last += a ** b / i
        except:
            last = b + a
            break
    return (last)
