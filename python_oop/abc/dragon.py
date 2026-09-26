#!/usr/bin/env python3
"""Using Mixin """

class SwimMixin():

    def fly(self):
        pass
    
    def swim(self):
        print("The creature swims!")

class FlyMixin():

    def fly(self):
        print("The creature flies!")
    
    def swim(self):
        pass

class Dragon(SwimMixin, FlyMixin ):

    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()

    dragon.swim()
    dragon.fly()
    dragon.roar()
