#!/usr/bin/python3
"""
This module defines an abstract class `Animal` which serves as a blueprint 
for animal-related subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.

    This class is meant to be inherited by subclasses that define specific 
    types of animals. It enforces the implementation of the `sound` method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.

        Each subclass must define this method to specify the sound 
        made by the respective animal.
        """
        pass


class Dog(Animal):
    """
    A subclass of `Animal` representing a dog.

    Implements the `sound` method to return the barking sound of a dog.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A subclass of `Animal` representing a cat.

    Implements the `sound` method to return the meowing sound of a cat.
    """

    def sound(self):
        return "Meow"
