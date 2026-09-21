#!/usr/bin/env python3
"""
4-square module

This module defines a Square class with an Area method.
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

    def area(self):
        """calculated an area of a square"""
        return self.__size ** 2

    def set_size(self,size):
        """Setter for __size with validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def get_size(self):
        """Returns the size attribute"""
        return self.__size
    size = property(get_size, set_size)