# Inheritance from father to son
# single inheritance

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


# Multilevel Inheritance

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