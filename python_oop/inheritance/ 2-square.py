#!/usr/bin/env python3
"""
Module square
Defines a square class.
"""
Rectangle = __import__('2-rectangle').Rectangle

class Square(Rectangle):
    """A square class."""
    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size) 
        self.__size = size
        
    
    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
