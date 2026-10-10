# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):     # Inherited
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")  # object created
print(dog.speak())  # accessing methods