#!/usr/bin/python3
"""
Module of rectangle.
"""


class Rectangle:
    """
    A class representing a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with width and height

        Args:
            width: the width of the rectangle, default is 0
            height: the height of the rectangle, default is 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Creates a string with the shape of the rectangle

        Returns:
            str: The shape of the rectangle in str
        """
        rec_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self.__height):
            for j in range(self.__width):
                rec_str = rec_str + "#"
            rec_str = rec_str + "\n"
        rec_str = rec_str.rstrip("\n")
        return rec_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle that
        can recreate an instance of the rectangle.

        Returns:
            str: A string that can be used by eval() to
            create a new Rectangle instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"
