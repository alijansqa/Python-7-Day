# ARGUMENTS
# Any information given to a function
from xmlschema.validators.schemas import name_attribute


def greet(name):
    print("Hi!", name)

greet("Ali")
greet("Jan")

# Multiple Arguments

def greet_full_name(firstname, lastname):
    print("Your full name is:",firstname, lastname)

greet_full_name("Ali","Jan")

# Arbitrary Arguments    *args
# unlimited arguments

print("Ali", "Jan", "..... so on")


def show_balance(*balance):
    print("Your Balance:", balance[0])  # In List form
    print("Your Balance:", balance[1])
    print("Your Balance:", balance[2])
    # call based on the defined number of args only
    # print("Your Balance:", balance[3])      <---- Not like this
show_balance("Bitcoin", "Solana", "Eth")



#  Keyword Arguments

def display_children(child1, child2, child3):
    print("Youngest child is:", child3)

display_children(child1="Ali", child2="Jan", child3="SQA")


# Arbitrary Keywords Arguments **kwargs

def show_details(**details):
    print("Your first name is: \n " + details["firstname"])
    print("Your last name is: \n" + details["lastname"])

show_details(firstname="Jane", lastname="Doe")


# Default Parameter Value

def my_country(country = "USA"):
    print("Your country is:" + country)

my_country("UK")
my_country("Spain")
my_country()
my_country()


# Return

def sum_3_numbers(a,b,c):
    return a+b+c

result = sum_3_numbers(5, 10, 15)
print(result)