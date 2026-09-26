#!/usr/bin/env python3
""" blueprint for creating and structuring derived 
classes. Python’s ABC package facilitates 
the creation of abstract base classes. """

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        # result = 3.14 * (self.radius ** 2)
        pi = 3.141592653589793
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        # result =  2 * 3.14 * self.radius
        pi = 3.141592653589793
        return 2 * pi  * self.radius



class Rectangle(Shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(shape):
    """Calls area and perimeter without checking the specific type."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


