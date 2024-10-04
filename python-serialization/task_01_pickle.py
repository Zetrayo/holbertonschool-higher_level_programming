#!/usr/bin/python3
"""not empty"""


import pickle


class CustomObject:
    """not empty"""

    def __init__(self, name, age, is_student):
        """not empty"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """not empty"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """not empty"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}")
        except (pickle.PicklingError, IOError) as e:
            print(f"Error while serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """not empty"""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object deserialized from {filename}")
            return obj
        except (pickle.UnpicklingError,
                FileNotFoundError, EOFError, IOError) as e:
            print(f"Error while deserializing object: {e}")
            return None
