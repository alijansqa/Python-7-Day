# Tuple
# ordered collection of items
# immutable, can not be changed

fruits = ("apple", "mango", "cherry")
print(fruits)
print(fruits[0])

#fruits[0] = "strawberry" will result in error

# EVERYTHING ELSE IS SAME

# Dictionary
# Unordered collection if key-value parts
# mmutable

student = {"name": "Ali", "PROFESSION": "Engineer", "Courses": ["Math","CompScience"]}
print(student)


student = {"name": "Ali", "PROFESSION": "Engineer", "Courses": 'Math, CompScience'}
print(student)

student["phone"] = "444-4444"
print(student)

student["Address"] = "10th Street"
print(student)