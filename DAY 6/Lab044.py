class LoginPage:
    def __init__(self, pageName):    # constructor ( parameterized constructor
        self.page_name = pageName  # page is attribute
    def display(self):   # function
        print(self.page_name)
LoginPage = LoginPage("LoginPage")
print(LoginPage.display())


# class & object example

class Faculty:
    def Data(self):
        self.id = int(input("Enter the ID: \n"))
        self.name = input("Enter the Name: \n")
        self.salary = float(input("Enter Faculty Salary: \n"))

    def showData(self):
        print("Faculty ID:\n", self.id)
        print("Faculty Name:\n", self.name)
        print("Faculty Salary:\n", self.salary)

a = Faculty()
a.Data()
a.showData()

# Direct Initialization

class Faculty:
    def __init__(self):    # Constructor # Dunder
        self.id = int(input("Enter the ID: \n"))
        self.name = input("Enter the Name: \n")
        self.salary = float(input("Enter Faculty Salary: \n"))

    def showData(self):
        print("Faculty ID:\n", self.id)
        print("Faculty Name:\n", self.name)
        print("Faculty Salary:\n", self.salary)

a = Faculty()
a.showData()


# Multiple Objects

class Faculty:
    def __init__(self):
        self.id = int(input("Enter the ID: \n"))
        self.name = input("Enter the Name: \n")
        self.salary = float(input("Enter Faculty Salary: \n"))

    def showData(self):
        print("Faculty ID:\n", self.id)
        print("Faculty Name:\n", self.name)
        print("Faculty Salary:\n", self.salary)

a = Faculty()
b = Faculty()
c = Faculty()
a.showData()
b.showData()
c.showData()
