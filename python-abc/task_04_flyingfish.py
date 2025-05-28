#!/usr/bin/python3
"""
This module defines classes representing different types of animals.

Includes `Fish` and `Bird` as base classes, and `FlyingFish`, which 
inherits behaviors from both, demonstrating multiple inheritance.
"""


class Fish:
    """
    Represents a fish with basic swimming behavior.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints the typical habitat of a fish (water).
    """

    def swim(self):
        """Prints a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message indicating that fish live in water."""
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with basic flying behavior.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints the typical habitat of a bird (sky).
    """

    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message indicating that birds live in the sky."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a unique creature that can both swim and fly.

    Inherits from both `Fish` and `Bird` and overrides their methods 
    to provide more accurate behavior for a flying fish.

    Methods:
        fly(): Prints a message indicating the flying fish is soaring.
        swim(): Prints a message indicating the flying fish is swimming.
        habitat(): Prints a message indicating the dual habitat of a flying fish.
    """

    def fly(self):
        """Prints a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message indicating the flying fish can live in both water and the sky."""
        print("The flying fish lives both in water and the sky!")
