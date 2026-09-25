#!/usr/bin/env python3
"""
Module rectangle
Defines a rectangle class.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class."""
    def __init__(self, width, height):
        """Initialize width and height after validation."""
        self.integer_validator("width" , width)
        self.__width = width

        self.integer_validator("height" , height)
        self.__height = height
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height
        
    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
        
        

