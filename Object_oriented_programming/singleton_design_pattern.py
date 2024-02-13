from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_data():
        pass

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton()
        return PersonSingleton.__instance

    def __init__(self):
        if PersonSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PersonSingleton.__instance = self

    @staticmethod
    def get_data():
        return "Data"

# Example usage
person1 = PersonSingleton.get_instance()
person2 = PersonSingleton.get_instance()

print(person1 == person2)  # Output: True


    