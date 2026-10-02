# String functions
#These methods are part of the core Python language and provide powerful tools for manipulating strings in various ways.

# for 1st letter Capital
s = "hello Ali"
print(s.capitalize())

# for Lower
s = "HELLO ALI JAN"
print(s.lower())

# for counting
s = "hello Ali"
print(s.count('o'))

# for center ( width, fillchar)
s = "hello Ali"
print(s.center(20, '*'))

# for encoding ('utf-8), errors='strict'
# returns encoded version of string as a byte object
s = ("hello word")
print(s.encode())

# for endswith(suffix, start, end)
# if string ends with specified suffied it will return true
s = 'hello ali'
print(s.endswith('ali'))

# for expand tabs (tabsize=8)
# replaces tabs in a string eith the specified number of spaces
s = 'hello\tAli'
print(s.expandtabs(4))

#find (sub, start, end)
# returns the lowest index in the string where substring sub is found
s = 'hello Ali'
print(s.find('Ali'))

# format (*arg, **kwargs)
# formats string usong specifiers
s = 'Hello Ali,{}'
print(s.format('Jan'))

# format_map(mapping)
# Formats the string using a dictionary.

s = 'Hello, {name}'
print(s.format_map({'name': 'world'}))  # Output: 'Hello, world'

#index(sub, start, end)
# Like find(), but raises ValueError when the substring is not found.

s = 'hello world'
print(s.index('world'))  # Output: 6

# isalnum()
# Returns True if all characters in the string are alphanumeric.

s = 'hello123'
print(s.isalnum())  # Output: True

# isalpha()
# Returns True if all characters in the string are alphabetic.

s = 'hello'
print(s.isalpha())  # Output: True

# isdecimal()
# Returns True if all characters in the string are decimal characters.

s = '123'
print(s.isdecimal())  # Output: True

# isdigit()
# Returns True if all characters in the string are digits.

s = '123'
print(s.isdigit())  # Output: True

# isidentifier()
# Returns True if the string is a valid identifier according to Python syntax.

s = 'hello_world'
print(s.isidentifier())  # Output: True

# islower()
# Returns True if all cased characters in the string are lowercase.

s = 'hello world'
print(s.islower())  # Output: True

# isnumeric()
# Returns True if all characters in the string are numeric characters.

s = '123'
print(s.isnumeric())  # Output: True

# isprintable()
# Returns True if all characters in the string are printable or the string is empty.

s = 'hello world'
print(s.isprintable())  # Output: True

# isspace()
# Returns True if all characters in the string are whitespace.

s = '   '
print(s.isspace())  # Output: True

# istitle()
# Returns True if the string is a title-cased string.

s = 'Hello World'
print(s.istitle())  # Output: True

# isupper()
# Returns True if all cased characters in the string are uppercase.

s = 'HELLO WORLD'
print(s.isupper())  # Output: True

# join(iterable)
# Joins the elements of an iterable to the string.

s = '-'
print(s.join(['hello', 'world']))  # Output: 'hello-world'

# ljust(width, fillchar)
# Returns a left-justified string of length width.

s = 'hello'
print(s.ljust(10, '*'))  # Output: 'hello*****'

# lower()
# Converts all characters in the string to lowercase.

s = 'HELLO WORLD'
print(s.lower())  # Output: 'hello world'

# lstrip(chars)
# Returns a copy of the string with leading characters removed.

s = '   hello world'
print(s.lstrip())  # Output: 'hello world'

# partition(sep)
# Splits the string at the first occurrence of sep.

s = 'hello world'
print(s.partition(' '))  # Output: ('hello', ' ', 'world')

# replace(old, new, count)
# Returns a string where all occurrences of old have been replaced by new.

s = 'hello world'
print(s.replace('world', 'Python'))  # Output: 'hello Python'

# rfind(sub, start, end)
# Returns the highest index in the string where substring sub is found.

s = 'hello world, hello Python'
print(s.rfind('hello'))  # Output: 13

#. rindex(sub, start, end)
# Like rfind(), but raises ValueError when the substring is not found.

s = 'hello world, hello Python'
print(s.rindex('hello'))  # Output: 13

# rjust(width, fillchar)
# Returns a right-justified string of length width.

s = 'hello'
print(s.rjust(10, '*'))  # Output: '*****hello'

# rpartition(sep)
# Splits the string at the last occurrence of sep.

s = 'hello world, hello Python'
print(s.rpartition(' '))  # Output: ('hello world, hello', ' ', 'Python')

# rsplit(sep=None, maxsplit=-1)
# Splits the string at the separator sep and returns a list of strings.

s = 'hello world hello Python'
print(s.rsplit(' ', 1))  # Output: ['hello world hello', 'Python']

# rstrip(chars)
# Returns a copy of the string with trailing characters removed.

s = 'hello world   '
print(s.rstrip())  # Output: 'hello world'

# split(sep=None, maxsplit=-1)
# Splits the string at the separator sep and returns a list.

s = 'hello world hello Python'
print(s.split())  # Output: ['hello', 'world', 'hello', 'Python']

# splitlines(keepends=False)
# Splits the string at line breaks and returns a list of lines.

s = 'hello\nworld'
print(s.splitlines())  # Output: ['hello', 'world']

# startswith(prefix, start, end)
# Returns True if the string starts with the specified prefix.

s = 'hello world'
print(s.startswith('hello'))  # Output: True

# strip(chars)
# Returns a copy of the string with leading and trailing characters removed.

s = '   hello world   '
print(s.strip())  # Output: 'hello world'

# swapcase()
# Converts uppercase characters to lowercase and vice versa.

s = 'Hello World'
print(s.swapcase())  # Output: 'hELLO wORLD'

# title()
# Returns a title-cased version of the string.
s = 'hello world'
print(s.title())  # Output: 'Hello World'

# translate(table)
# Returns a copy of the string in which each character has been mapped through a given translation table.

# Translation table to replace 'h' with 'j'
trans = str.maketrans('h', 'j')
s = 'hello world'
print(s.translate(trans))  # Output: 'jello world'

# upper()
# Converts all characters in the string to uppercase.
s = 'hello world'
print(s.upper())  # Output: 'HELLO WORLD'

# zfill(width)
#Pads the string on the left with zeros to fill width.

s = '42'
print(s.zfill(5))  # Output: '00042'