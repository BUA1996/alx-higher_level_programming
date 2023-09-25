#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divide = a / b
    except (ZeroDivisionError, TypeError):
        divide = None
    finally:
        print("Inside Result: {}".format(divide))
    return (divide)
