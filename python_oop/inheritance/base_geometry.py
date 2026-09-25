#!/usr/bin/env python3
"""
Module base_geometry
Defines a BaseGeometry class.
"""
class BaseGeometry:
    """A BaseGeometry class."""
    def area(self):
        raise Exception("not implemented in this class.")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")