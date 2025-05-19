#!/usr/bin/python3


class Square:
    __size = None

    def __init__(self, __size):
        if isinstance(__size, int):
            self.__size = __size
        else:
            return None
