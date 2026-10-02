# Operators
from email.policy import default

a = 10   # arithmatic op
b = 20   # can be minus q=-20   # = is assignment op
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# unary +
a = 5
print(a) # unary + is by default

# unary -
b = 5
print(-b)

# logical negation (not)
flag = True
print(not flag)

# bitwise ~
z = 5
print(~z)

# identity op
# normal variables hava same value they are stored in same memory
s = 5
v = 5
print(s is v)
print(s is not v)

# lists are not stored in same memory
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)


# is and == are different

# Logical

a = True
b = False

print(a and b)
print(a or b)
print(a ^ b)
print(a~b)


# Turnery op

x = 10
y = 20

print("x is greater" if x>y else "y is greater")

# concatenation

str1 = "Ali"
str2 = "Jan"
str3 = str1 + str2
print(str3)

# string with non string
str4 = "Ali,"
num = 10
# str5 = str4 + num This will cause in TypeError pass it through string to make it run
str5 = str4 + str(num)

print(str5)