# Constructor
# Used in API, Web automation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("toyota", "corolla", 2020)
print(my_car.display_info())

#
class student:
   name = "ali"

s1 = student()
print(s1)

#
class student:
    name = "ali"

s1 = student()
print(s1.name)

#
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("New Student has been added!")

s1 = student( "Name: Ali\t", "Marks: 100")
print(s1.name, s1.marks)

s2 = student( "Name: Jan\t", "Marks: 100")
print(s2.name, s2.marks)
