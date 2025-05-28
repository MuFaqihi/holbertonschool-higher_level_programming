#!/usr/bin/python3
"""
Module defining geometric shapes using duck typing.

Includes an abstract base class `Shape` with methods for calculating
area and perimeter. The module also provides concrete implementations
for `Circle` and `Rectangle`.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Enforces the implementation of `area` and `perimeter` methods 
    in subclasses, allowing polymorphic behavior.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Returns the calculated area of the circle.
        perimeter(): Returns the calculated perimeter (circumference) of the circle.
    """

    def __init__(self, radius):
        self.__radius = abs(radius)  # Ensure radius is non-negative

    def area(self):
        """Computes the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Computes the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    A class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area(): Returns the calculated area of the rectangle.
        perimeter(): Returns the calculated perimeter of the rectangle.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints the area and perimeter of the given shape.

    Parameters:
        shape (Shape): An instance of a shape implementing `area` and `perimeter`.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
