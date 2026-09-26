#!/usr/bin/env python3
"""Module defining Fish, Bird, and FlyingFish classes to demonstrate multiple inheritance."""


# 1. Create Fish class
class Fish:
    """Class representing a fish."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


# 2. Create Bird class
class Bird:
    """Class representing a bird."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


# 3. Create FlyingFish inheriting from Fish and Bird
class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from both Fish and Bird."""

    # 4. Override fly
    def fly(self):
        print("The flying fish is soaring!")

    # 5. Override swim
    def swim(self):
        print("The flying fish is swimming!")

    # 6. Override habitat
    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# Execution block for steps 7, 8, and 9
if __name__ == "__main__":
    # 7. Instantiate FlyingFish
    flying_fish = FlyingFish()

    # 8. Call fly, swim, and habitat methods
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    # 9. Inspect Method Resolution Order (MRO)
    print("\nMethod Resolution Order (MRO):")
    print(FlyingFish.__mro__)