#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class defines an abstract method `sound` that must be implemented
    by any subclass to provide the specific sound the animal makes.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be overridden to
        return the sound of the animal.

        Returns:
            str: The sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Class representing a Dog, which is a subclass of Animal.
    """

    def sound(self):
        """
        Implementation of the `sound` method for the Dog class.

        Returns:
            str: The sound a dog makes, which is 'Bark'.
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a Cat, which is a subclass of Animal.
    """

    def sound(self):
        """
        Implementation of the `sound` method for the Cat class.

        Returns:
            str: The sound a cat makes, which is 'Meow'.
        """
        return "Meow"
