#!/usr/bin/env python3
"""
1-rectangle module

This module defines a Rectangle class.
"""
class Rectangle:
    """Defines a rectangle."""
    def __init__(self,width=0, height=0):
        """Initializes a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        
    @width.setter
    def width(self , value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def width(self):
        """Returns the width attribute"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attrabute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def height(self):
        """Returns the height attribute"""
        return self.__height

    height = property(height, height)
    width = property(width, width)