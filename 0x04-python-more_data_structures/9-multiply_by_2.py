#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    keys = list(copy.keys())

    for num in keys:
        copy[num] *= 2
    return (copy)
