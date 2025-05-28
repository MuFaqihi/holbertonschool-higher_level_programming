#!/usr/bin/python3
"""
This module defines the `VerboseList` class, which extends Python's 
built-in `list` to provide informative print statements when modifying 
the list.
"""

from abc import ABC, abstractmethod


class VerboseList(list):
    """
    A subclass of `list` that provides detailed logging when elements 
    are added, removed, or modified.
    """

    def append(self, object):
        """Appends an item to the list and prints a confirmation message."""
        print("Added [{}] to the list.".format(object))
        return super().append(object)

    def extend(self, iterable):
        """Extends the list with multiple items and prints the count."""
        print("Extended the list with [{}] items.".format(len(iterable)))
        return super().extend(iterable)

    def remove(self, value):
        """Removes a specified item from the list and prints a message."""
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def pop(self, index=-1):
        """Removes and returns an item at the given index, with a message."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
