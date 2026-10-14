# Inheritance from father to son
# single inheritance

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



class Father:
    def bhk10(self):
        print("10 Bedroom Kitchen Inherited ")

class Son(Father):
    pass    # son has nothing

s = Son()
s.bhk10()

#
class Father:
    def bhk(self):
        print("10 Bedroom Kitchen Inherited ")

class Son(Father):
    def bhk(self):
        print("2 Bedroom Kitchen")

s = Son()   # son will be prioritized because we have created the object
s.bhk()



# Multi-level Inheritance

class Grandfather():
    def lambo(self):
        print("Lamborghini Inherited from Grandfather")

class Father(Grandfather):
    def bhk(self):
        print("10 Bedroom Kitchen Inherited ")

class Son(Father):
    def bhk(self):
        print("2 Bedroom Kitchen")

s = Son()   # son will be prioritized because we have created the object
s.bhk()
s.lambo()


# Multi-Level

class Car:
    @staticmethod
    def start():
     print("Car Started...")
    @staticmethod
    def stop():
     print("Car Stopped.")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()
print(car1.type)
