 # Print grade based on score

score = int(input("Enter Your Marks Obtained: \n"))

if score >= 90 and score <= 100:
    print("A GRADE")
elif score >= 80 and score <=89:
    print("B GRADE")
elif score >= 70 and score <=79:
    print("C GRADE")
elif score >= 60 and score >= 69:
    print("C GRADE")
elif score <= 50 and score >= 59:
    print("D GRADE")
else:
    print("FAIL")