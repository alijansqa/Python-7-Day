# for 3 number if condition

num1 = int(input("Enter 1st number:\n"))
num2 = int(input("Enter 2nd Number:\n"))
num3 = int(input("Enter 3rd Number:\n"))

if num1 > num2 and num1 > num3:
    print(num1)

elif num2 > num1 and num2 > num3:
    print(num2)

else:
    print(num3)