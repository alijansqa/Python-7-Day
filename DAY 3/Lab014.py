# string is immutable its value can not be changed

"""string = 'Ali Jan'
string[0] = 'X'   Will result in error"""

# slicing

my_str = "My name is Ali Jan & I am a Software Engineer"
print(my_str[0:2])
# [start:end:steps]   step is by default one [0:2:1]
print(my_str[0:18:2])

# for any length output
print(my_str[11:len(my_str)])

# for reversing the string
print(my_str[::-1]) # you can put any numbers also in [2:2:-1] if you need

