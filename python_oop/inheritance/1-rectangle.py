#!/usr/bin/env python3
"""
Module rectangle
Defines a rectangle class.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class."""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(width , width)
        self.__width = width
        
        BaseGeometry.integer_validator(height , height)
        self.__height = height
        
        

