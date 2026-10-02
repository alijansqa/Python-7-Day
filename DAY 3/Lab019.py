# Numeric Literals
from xmlschema.validators.helpers import non_negative_int_validator

a = 0b1010 # binary
b = 100 # decimal | ascii
c = 0o310 # octal
d = 0x12c # hexadecimal
float1 = 10.5 # float
float2 = 1.5e2
x = 3.14j # complex
char = "Hello Ali Jan" # string
unicode = u"\u00dcnic\u00f6de" # unicode
raw_str = r"raw \n string" # raw string
print(a,b,c,d,float1,float2,x,char,unicode,raw_str)

multiline_str = """This is a Multiline
which
can
be
any length"""

print(multiline_str)


# boolean literal
x = (1 == True)
y = (1 == False)

a = True + 4
b = False + 10

print(x,y,a,b)

# special literal
drink = "Available"
food = "none"
print(drink, food)

# Tuples
#also kind of list
tuple_num = (1,2,3,4,5)
print(tuple_num)

# alphabets

alphabets = {'a':'apple', 'b':'banana', 'c':'cat'}
print(alphabets)

# dictionary
vowel = {'a','b','c','d','e','f','g'} # also set
print(vowel)