#!/usr/bin/python3
"""
Module that defines a Square class.

This module provides a `Square` class that allows for setting and retrieving
the size of a square, calculating its area, and printing a visual representation
of the square using the `#` character.

Example:
    >>> square = Square(3)
    >>> square.my_print()
    ###
    ###
    ###
"""


class Square:
    """Represents a square with size validation and operations.

    Attributes:
        __size (int): Private instance attribute representing the square's size.
    """

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a visual representation of the square using `#` characters.

        If `size` is 0, it prints an empty line.

        Example:
            >>> square = Square(3)
            >>> square.my_print()
            ###
            ###
            ###
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
