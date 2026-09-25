#!/usr/bin/env python3
"""
Module square
Defines a square class.
"""
Rectangle = __import__('base_geometry').Rectangle

class Square(Rectangle):
    """A square class."""
    def __init__(self, size):

        self.vainteger_validator("size", size)
        self.__size = size
        # super().__init__(size, size) 
    
    def area(self):
        return self.__size ** 2
