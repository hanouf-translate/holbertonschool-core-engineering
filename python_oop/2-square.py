#!/usr/bin/env python3
"""
1-square module

This module defines a Square class.
"""

class Square:
    """Defines a square."""
    def __init__(self,size=0):
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """Initializes a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size



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

    def __set_width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def width(self):
        """Returns the width attribute"""
        return self.__width
        

    def __set_height(self, value):
        """Sets the height attrabute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def height(self):
        """Returns the height attribute"""
        return self.__height

    height = property(height, __set_height)
    width = property(width, __set_width)
    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height
        
    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)