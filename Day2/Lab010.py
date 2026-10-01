# Python is Dynamic Typed Language
#1
a = 10
b = a
c = b

print(a)
print(b)
print(c)

#2 you can change variable value even in middle
a = 10
b = a
b= 60
c = b

print(a)
print(b)
print(c)

#3
a = 10
b = a
c = b
a = "Ali Jan"
print(a)
print(b)
print(c)

# if you want to find the type
a = 10
b = "Ali Jan"
c = 3.14
AliJan = True

print(type(a))
print(type(b))
print(type(c))
print(type(AliJan))