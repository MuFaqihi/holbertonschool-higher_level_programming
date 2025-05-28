#!/usr/bin/python3
"""
This module defines the `CountedIterator` class, an iterator wrapper 
that tracks the number of items retrieved.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of elements accessed.

    Attributes:
        iterable (iterable): The underlying iterable to iterate over.
        count (int): The number of items accessed from the iterator.

    Methods:
        __next__(): Retrieves the next item from the iterable and increments the count.
        get_count(): Returns the total number of items accessed.
    """

    def __init__(self, iterable):
        self.__iterable = iter(iterable)
        self.__count = 0

    def __iter__(self):
        """Returns itself as an iterator."""
        return self

    def __next__(self):
        """Returns the next item from the iterable and updates the count."""
        try:
            item = next(self.__iterable)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the number of items retrieved from the iterable."""
        return self.__count
