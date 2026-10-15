# Abstracrion
# Hiding implementation details of a class
# only showing important details to the user

class Car:
    def __init__(self):
        self.key = False                    # All these True/False (unnecessary stuf)
        self.acc = False                    # won't be visible in the output that is abstraction
        self.clutch = False
        self.brk = False

    def start(self):
        self.key = True
        self.acc = True
        self.clutch = True
        print("Car Started...")
car = Car()
car.start()
