# Recursion
# A method of solving problems where the function can call itself
# each recursion call should move closure to a base case that stops the recursion
# You can not call infinite times you should have an exit

def rec_count(number):
    print(number)
    if (number==0): # EXIT CONDITION
        return 0
    else :
        rec_count(number-1)
rec_count(5)


"""
def rec_count(number):
    print(number)
        rec_count(number-1)   # WILL KEEP RECURSING
rec_count(5)"""   #


# Factorial
# 5*4*3*2*1

def factorial(n):
    if n==1:
        return 1;
    else:
        return n*factorial(n-1)

print(factorial(5))