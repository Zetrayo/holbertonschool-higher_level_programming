# Python abc

This directory is dedicated to the study of python

## Content

|File|Use|
|----------------|----------------------------------|
|task_00_abc.py|Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.|
|task_01_duck_typing.py|Create an abstract class named Shape with two abstract methods: area and perimeter.
Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class should provide implementations for the area and perimeter methods.
Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
Test the shape_info function with instances of both Circle and Rectangle.|
|task_02_verboselist.py|Setting up the VerboseList Class:

Define a class VerboseList that inherits from the built-in list class.
Within VerboseList, override the methods that modify the list: append, extend, remove, and pop.
Implementing Notifications:

For the append method: After adding the item to the list, print a message like “Added [item] to the list.”
For the extend method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
For the remove method: Before removing the item from the list, print a message like “Removed [item] from the list.”
For the pop method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.
Testing:

Instantiate a VerboseList object.
Test all the overridden methods (append, extend, remove, and pop) and ensure that the appropriate messages are printed for each operation.|
|task_03_countediterator.py|Setting up the CountedIterator Class:

Define a class CountedIterator.
In the constructor (__init__), initialize two attributes: the iterator object (using the iter function) and a counter to track the number of items iterated.
Provide a method get_count to return the current value of the counter.
Overriding the next Method:

Within the CountedIterator class, override the __next__ method.
In this method, increment the counter each time the __next__ method is called.
Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the StopIteration exception.
Testing:

Instantiate a CountedIterator object using a list or another iterable.
Iterate over items using a loop or manual calls to the __next__ method.
Use the get_count method to retrieve and print the number of items that have been fetched.|
|task_04_flyingfish.py|Parent Classes Setup:

Create a Fish class with methods swim (which prints “The fish is swimming”) and habitat (which prints “The fish lives in water”).
Create a Bird class with methods fly (which prints “The bird is flying”) and habitat (which prints “The bird lives in the sky”).
Implementing FlyingFish:

Construct a FlyingFish class that inherits from both Fish and Bird.
Override the fly method to print “The flying fish is soaring!”.
Override the swim method to print “The flying fish is swimming!”.
Override the habitat method to print “The flying fish lives both in water and the sky!”.
Testing and MRO Exploration:

Instantiate an object of the FlyingFish class.
Call the fly, swim, and habitat methods and observe the outputs.
Use the mro() method or the .__mro__ attribute on the FlyingFish class to investigate the method resolution order. For instance, print(FlyingFish.mro()).|
|task_05_dragon.py|Creating Mixins:

Design a mixin called SwimMixin with a method swim that prints “The creature swims!”.
Design another mixin called FlyMixin with a method fly that prints “The creature flies!”.
Implementing Dragon:

Construct a class named Dragon that inherits from both SwimMixin and FlyMixin.
Within the Dragon class, you can add additional methods or attributes if desired, such as roar, which could print “The dragon roars!”.
Testing the Dragon’s Abilities:

Instantiate an object of the Dragon class named draco.
Demonstrate draco‘s abilities by calling the swim, fly, and (if implemented) roar methods.|

## Contributors

José Puertas

## Special Mention

# Holberton School
