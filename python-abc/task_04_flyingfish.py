#!/usr/bin/python3

class Fish:
    """
    A class representing a fish.

    This class provides methods for actions typical of a fish,
    such as swimming and describing its habitat.
    """

    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message describing the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.

    This class provides methods for actions typical of a bird,
    such as flying and describing its habitat.
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message describing the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, which can both swim and fly.

    This class overrides the behavior of both Fish and Bird, providing
    unique implementations of flying, swimming, and its habitat.
    """

    def fly(self):
        """
        Prints a message indicating that the flying fish is soaring in the air.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the
        flying fish is swimming in the water.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message describing the dual habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")
