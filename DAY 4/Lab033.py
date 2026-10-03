# factorial

number = int(input("Enter the number:\n"))
fact = 1

if number < 0:
    print("Factorial:", number)

elif number == 0:
    print("Factorial:", -1)

else:
    for i in range(1, number + 1):
        fact = fact * i

        print("Factorial:", fact)