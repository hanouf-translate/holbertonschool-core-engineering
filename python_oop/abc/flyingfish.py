#!/usr/bin/env python3
""" blueprint for creating and structuring derived 
classes. Python’s ABC package facilitates 
the creation of abstract base classes. """

from abc import ABC, abstractmethod

class Fish():

    def swim(self):
        return "The fish is swimming"
    
    def habitat(self):
        return "The fish lives in water"
    
class Bird():
    def fly(self):
        return "The bird is flying"
    
    def habitat(self):
        return "The bird lives in the sky"

class FlyingFish(Fish , Bird):
    def fly(self):
        return "The flying fish is soaring!"
    
    def swim(self):
        return "The flying fish is swimming!"
    
    def habitat(self):
        return "The flying fish lives both in water and the sky!"

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()