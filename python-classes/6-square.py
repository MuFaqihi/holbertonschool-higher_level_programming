#!/usr/bin/python3


class Square:
    def __init__(self, __size=0, __position=(0, 0)):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
        if not isinstance(__position, tuple) or len(__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(type(i) is int and i >= 0 for i in __position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = __position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(type(i) is not int for i in value) or all(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
