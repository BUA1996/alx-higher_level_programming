#!/usr/bin/python3

"""defines a class square"""
class Square:
    """Instance"""
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """setter"""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    @property
    def position(self):
        """setter position"""
        return (self.__position)
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or not
                all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
    def area(self):
        return (self.__size * self.__size)
    def my_print(self):
        if self.__size == 0:
            print('')
            return
        [print('') for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for y in range(0, self.position[0])]
            [print('#', end='') for q in range(0, self.__size)]
            print("")

