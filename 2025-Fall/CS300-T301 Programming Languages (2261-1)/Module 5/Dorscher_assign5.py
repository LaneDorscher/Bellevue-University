# Dorscher_assign5.py
# Author: Lane Dorscher
# Date: 10/12/2025
# Description:
# Demonstrates the creation of an abstract class and a concrete class in Python.

from abc import ABC, abstractmethod

# Abstract class
class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass

# Concrete class
class Player(GameCharacter):
    def attack(self):
        print("Player attacks with a sword!")

def main():
    hero = Player()
    print(f"Concrete class name: {hero.__class__.__name__}")
    print(f"Base class name: {Player.__bases__[0].__name__}")
    hero.attack()

if __name__ == "__main__":
    main()