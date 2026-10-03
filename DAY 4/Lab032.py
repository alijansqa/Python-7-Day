# trigonometry triangle program

side1 = float(input("1st side:\n"))
side2 = float(input("2nd side:\n"))
side3 = float(input("3rd side:\n"))

if side1 == side2 == side3:
    print("Equalateral")

elif side1 == side2 or side1 == side3 or side2 == side3:
    print("ISO")
else:
    print("Scalene")