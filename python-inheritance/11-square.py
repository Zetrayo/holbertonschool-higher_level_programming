#!/usr/bin/python3
"""
Module of geometry.
"""


class BaseGeometry():
    """
    A class of geometry.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
Module of rectangle.
"""


class Rectangle(BaseGeometry):
    """
    A class of rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    A class of square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return ("[Square] {}/{}".format(self._Rectangle__width,
                                        self._Rectangle__height))
