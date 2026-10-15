
# you can handle multiple errors like server fetching error etc
try:
    num = int(input("Enter your number:"))
    a = [6,3]
    print(a[num])
except ValueError:
     print("Number not an integer")

except IndexError:
     print("Index Error")