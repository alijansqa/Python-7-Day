# SET
# Unordered collection of unique items
# mutable but do not allow duplicate elements

set = {"apple", "dates", "cherry", "banana"}
print(set)

set = {"apple", "dates", "cherry", "banana"}
set.add("strawberry")
print(set)

# same functions can be applied

set.remove("apple")
print(set)

# to find an element
print("dates" in set)

set.add("strawberry")  # Will not create duplicate
print(set)

# set union

set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2)
# INTERSECTION
print(set1 & set2)
# for difference
print(set1 - set2)
# symmetric difference
print(set1 ^ set2)
# for reverse
print(set2 - set1)

myset = {"ALI JAN"}
myset1 = {"SQA"}
print(myset | myset1 )
