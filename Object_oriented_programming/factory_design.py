'''Imagine you're in a toy factory where different kinds of toys are made. Sometimes, you want to make a toy without knowing exactly what kind it will be until you make it.

That's where the Factory Design Pattern comes in!

Factory Boss: In our toy factory, we have a boss who knows how to make different kinds of toys. But the boss doesn't make the toys directly. Instead, the boss tells the workers what kind of toy to make.
Toy Workers: We have different workers who are good at making specific types of toys. For example, we have workers who make dog toys, cat toys, and maybe even bird toys.
Orders: When someone wants a toy, they tell the boss what kind of toy they want. The boss then tells the right worker to make that toy.
Toy Delivery: After the worker finishes making the toy, the boss gives it to the person who ordered it.
So, the Factory Design Pattern is like having a boss (the factory) that knows which worker (class) to ask to make the toy (object) you want. You don't need to worry about how the toy is made or who makes it. You just ask the boss for the toy you want, and the boss takes care of the rest!

In our example code, we have a factory that makes animal toys. There are workers for making dog toys and cat toys. When someone wants a toy, they ask the factory for it, and the factory decides whether to make a dog or cat toy, depending on what's requested. Then, the factory gives the toy to the person who asked for it. It's simple and organized!'''

from abc import ABC, abstractmethod

# Step 1: Define the Toy interface or base class
class AnimalToy(ABC):
    @abstractmethod
    def play(self):
        pass

# Step 2: Create concrete toy classes
class DogToy(AnimalToy):
    def play(self):
        return "The dog toy squeaks!"

class CatToy(AnimalToy):
    def play(self):
        return "The cat toy has a bell!"

# Step 3: Create the Toy Factory
class ToyFactory:
    def create_toy(self, toy_type):
        if toy_type == "dog":
            return DogToy()
        elif toy_type == "cat":
            return CatToy()
        else:
            raise ValueError("Invalid toy type")

# Step 4: Client Code
if __name__ == "__main__":
    toy_factory = ToyFactory()

    # Ordering dog toy
    dog_toy = toy_factory.create_toy("dog")
    print(dog_toy.play())  # Output: The dog toy squeaks!

    # Ordering cat toy
    cat_toy = toy_factory.create_toy("cat")
    print(cat_toy.play())  # Output: The cat toy has a bell!
