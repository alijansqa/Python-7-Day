# if you do not want to print e

a = input("Enter the Number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
       print(f"{int(a)} x {i} = {int(a) * i}")
except Exception as e:
      print("Some error occured")

print("Table is finished")
print("Extra Lines")


# clean code without using e

a = input("Enter the Number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
       print(f"{int(a)} x {i} = {int(a) * i}")
except:
    print("Invalid Input!")

print("Table is finished")
print("Extra Lines")

