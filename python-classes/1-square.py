#!/usr/bin/python3
"""this is module defines a class reprenting a square.
"""


class Square:
    """this is class that defines a square.
    """
    __size = None

    def __init__(self, __size):
        if isinstance(__size, int):
            self.__size = __size
        else:
            return None
