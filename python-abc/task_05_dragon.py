#!/usr/bin/python3

class SwimMixin:
    """
    A mixin class that provides swimming ability to creatures.

    This mixin adds a swim method, which can be inherited by any class
    that represents a creature capable of swimming.
    """

    def swim(self):
        """
        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying ability to creatures.

    This mixin adds a fly method, which can be inherited by any class
    that represents a creature capable of flying.
    """

    def fly(self):
        """
        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, which can both swim and fly.

    The Dragon class inherits from both SwimMixin and FlyMixin to gain
    the abilities to swim and fly, and it defines
    its own behavior such as roaring.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
