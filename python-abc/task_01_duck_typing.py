#!/usr/bin/python3
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    This class defines two abstract methods: `area` and `perimeter`,
    which must be implemented by any subclass to calculate the area
    and perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to compute the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to compute the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle, which is a subclass of Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Computes the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Computes the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle, which is a subclass of Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(value):
    """
    Prints the area and perimeter of the given shape.

    Args:
        value (Shape): An object that is an instance of a subclass of Shape.
    """
    print("Area: {}".format(value.area()))
    print("Perimeter: {}".format(value.perimeter()))
