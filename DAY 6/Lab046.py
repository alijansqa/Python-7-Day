# Inheritance
# single inheritance


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



# 
class Car:
    @staticmethod
    def start():
     print("Car Started...")
    @staticmethod
    def stop():
     print("Car Stopped.")

class Cadillac(Car):
    def __init__(self, name):
        self.name = name

car1 = Cadillac("\nCar: \nEscalade")
car2 = Cadillac("\nCar: \nVistiq")

print(car1.name, car2.name)


# we can also add color right after class

class Car:
    color = "black"
    @staticmethod
    def start():
     print("Car Started...")
    @staticmethod
    def stop():
     print("Car Stopped.")

class Cadillac(Car):
    def __init__(self, name):
        self.name = name

car1 = Cadillac("\nCar: \nEscalade")
car2 = Cadillac("\nCar: \nVistiq")

print(car1.color)
print(car1.name, car2.name)
