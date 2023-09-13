#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    number = 0
    avrg = 0
    for num in my_list:
        number += num[0] * num[1]
        avrg += num[1]
    return (number / avrg)
