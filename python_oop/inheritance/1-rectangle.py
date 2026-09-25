#!/usr/bin/env python3
"""
Module rectangle
Defines a rectangle class.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle class."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(width , width)
        BaseGeometry.integer_validator(height , height)

