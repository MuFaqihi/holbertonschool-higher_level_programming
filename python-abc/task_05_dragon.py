#!/usr/bin/python3
"""
This module defines mixins for swimming and flying behavior.

It includes `SwimMixin` and `FlyMixin` to add specific abilities to 
classes that inherit them. The `Dragon` class combines both behaviors 
and introduces a unique ability to roar.
"""


class SwimMixin:
    """
    A mixin that provides swimming functionality.

    Methods:
        swim(): Prints a message indicating that the creature swims.
    """

    def swim(self):
        """Prints a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin that provides flying functionality.

    Methods:
        fly(): Prints a message indicating that the creature flies.
    """

    def fly(self):
        """Prints a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A mythical creature that can both swim and fly.

    Inherits abilities from `SwimMixin` and `FlyMixin` and 
    introduces a unique ability to roar.

    Methods:
        roar(): Prints a message indicating the dragon is roaring.
    """

    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
