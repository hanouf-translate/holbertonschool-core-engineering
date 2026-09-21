#!/usr/bin/env python3
"""
1-square module

This module defines a Square class.
"""

class Square:
    """Defines a square."""
    def __init__(self,size):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        """Initializes a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size