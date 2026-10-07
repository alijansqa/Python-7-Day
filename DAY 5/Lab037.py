# Data Types
# List, Set, Tuple & Dictionary
# List: Ordered Collection of items

fruits = ["apple", "banana", "cherry", "apple"]   # can be duplicate items
print(fruits[0])  # index based

# Adding element to a list

fruits.append("dates")
print(fruits)

fruits.remove("apple") # will remove the first "apple"
print(fruits)


fruits.remove("apple")  # will remove the 2nd " apple"
print(fruits)

# for slicing
print(fruits[1:3])  # index starts with 0, 1:3 means 1 to 2

# for reverse
fruits.reverse()
print(fruits)

# for copying
fruits.copy()
print(fruits)