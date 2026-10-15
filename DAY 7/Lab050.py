# Exception Handling
# we use try except code
# process of responding ti unwated or unexpected events
# deals with events to avoid program or system crashing

# suppose we write a code and it runs normally

a = input("Enter the Number:")
print(f"Multiplication table of {a} is:")
for i in range(1,11):
    print(f"{int(a)} x {i} = {int(a) * i}")

print("Table is finished")


#  but we out wrong input in output and try to handle that exception

a = input("Enter the Number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
       print(f"{int(a)} x {i} = {int(a) * i}")
except Exception as e:
    print(e)

print("Table is finished")
print("Extra Lines")
