# Polymorphism   ( Operator overloading)
# when we implement or change meaning our classes and objects it's implementation of polymorphism
# When same operator is allowed to have different meaning acc to context
# dunder functions are the ones where we use __ before them
# a+b, a-b, a*b, a/b, a%b


# many forms of +
# different outputs
# meaning of + will be changed
print(1+2)   # addition
print("Ali" + "Jan")   # concatenate
print([1,2,3] + [4,5,6])   # merge


# addition

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNo(self):
        print(self.real, "i +", self.img, "j")

num1 = Complex(5, 10)
num1.showNo()
num2 = Complex(20, 25)
num2.showNo()

# Now logic to add complex numbers


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNo(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(5, 10)
num1.showNo()
num2 = Complex(20, 25)
num2.showNo()
num3 = num1.add(num2)
num3.showNo()

#addition simplified with dunder


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNo(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(5, 10)
num1.showNo()
num2 = Complex(20, 25)
num2.showNo()
num3 = num1 + num2
num3.showNo()


# subtraction

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNo(self):
        print(self.real, "i +", self.img, "j")

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(5, 10)
num1.showNo()
num2 = Complex(20, 25)
num2.showNo()
num3 = num1 - num2
num3.showNo()