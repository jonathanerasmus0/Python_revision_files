'''Imagine you have different animals, each making a sound. Now, let's say you have a command to make all these animals "speak" without knowing exactly which animal it is. Polymorphism in Python lets you do just that!

In simple terms, polymorphism means that different objects can be treated the same way even though they might be of different types. In our case, it means we can call the same method on different animal objects, and they will each make their own sound.'''

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Let's make our animals speak
if __name__ == "__main__":
    animals = [Dog(), Cat()]

    for animal in animals:
        print(animal.speak())
