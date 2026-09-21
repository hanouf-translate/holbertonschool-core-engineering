#!/usr/bin/env python3
"""
5-square module

This module defines a Square class with an Area method.
"""

class Square:
    """Defines a square."""
    def __init__(self,size=0,position=(0, 0)):
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")

        """Initializes a square with a given size.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__position[1]):
                print()
                
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        if self.__size == 0:
            return ""
        else:
            lines = []
            for _ in range(self.__size):
                lines.append("#" * self.__size)
            return "\n".join(lines)

    def  position(self, value):
        """Setter for __position with validation."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def position(self):
        """Returns the position attribute."""
        return self.__position
    position = property(position, position)