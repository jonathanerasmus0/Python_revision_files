'''Imagine you have a drawing of different animals. But you don't draw the animals directly. Instead, you have a special template with outlines of animals, like a coloring book. This template gives you the basic shape of each animal, and you can use it to draw different animals more easily.

In Python, an abstract class is like that special template. It's a blueprint for other classes. It gives them a basic outline or structure, but you can't make a direct object out of it. It's just there to help other classes be more organized and similar.'''
from abc import ABC, abstractmethod

# This is our abstract class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Specific animals inherit from our abstract class
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Let's use our animals
if __name__ == "__main__":
    dog = Dog("Buddy")
    print(dog.name + " says: " + dog.make_sound())  # Output: Buddy says: Woof!

    cat = Cat("Whiskers")
    print(cat.name + " says: " + cat.make_sound())  # Output: Whiskers says: Meow!
