#!/usr/bin/python3

"""
This module provides a function for safely adding two numbers.
Both inputs must be integers or floats; otherwise, a TypeError is raised.
"""

def add_integer(a, b=98):

    """
    Adds two numbers, converting floats to integers before performing the operation.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, default=98): The second number to add.

    Returns:
    int: The sum of the two numbers as an integer.

    Raises:
    TypeError: If either a or b is not an integer or float.

    Example:
    >>> add_integer(1, 2)
    3
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
