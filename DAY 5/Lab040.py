# Python Lambda
# A Lambda function is a small anonymous function
# lambda arguments : expression
# in simple terms to shorten the code
# to change something to function

# general code
def num_add_10(num):
    return num+10

result = num_add_10(1)
print(result)

# Lambda code
result = lambda num: num+10
x = result(1)
print(x)

x = lambda a, b : a + b
print(x(5, 10))

x = lambda num1, num2, num3 : num1 + num2 * num3
print(x(5, 10, 15))