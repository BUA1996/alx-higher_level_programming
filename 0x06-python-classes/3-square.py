#!/usr/bin/python3

"""Defines a class Square"""
class Square:
    """Represents a class instance"""
    def __init__(self, size=0):
        """Initialize a new square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Return area of the sqaure"""
        return (self.__size * self.__size)
