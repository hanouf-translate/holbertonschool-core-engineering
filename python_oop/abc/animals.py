#!/usr/bin/env python3
""" blueprint for creating and structuring derived 
classes. Python’s ABC package facilitates 
the creation of abstract base classes. """

from abs import ABC , abstractmethod

class Animal(ABC):
    """Animal abstract class """
    @abstractmethod
    def sound(self):
        pass
    

class Dog(Animal):
    """Dog class """
    def sound(self):
        return "Bark"

class Cat(Animal):
     """Cat class """
    def sound(self):
        return "Meow"