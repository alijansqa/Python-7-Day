# File I/O (File handling)
# first open the file. For that we use open() function
# takes 2 arguments; name of file and the mode you want the file in

f = open('myfile.txt', 'r')    # it'll give error because no file exists for now

# r = read     to open file in read only mode, will give error if no file exist
# w = write    to open file in write only mode, will create a new file if it doesn't exist
# a = append   to open file in append only mode, will create a new file if it doesn't exist


# now we will create the file
# myfile.txt

# it will not end in error. you can run the above command

# to open the file and bring it's text here we use
f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# to write
f = open('myfile.txt', 'w')
f.write('Hello')     # it will over ride everything existing in the file

# to append
f = open('myfile.txt', 'a')
f.write(' I am Ali Jan')     # it will not over ride everything existing in the file, it'll add text at the end
f.close()

# to close a file without close() function
with open('myfile.txt', 'a')  as f:
    f.write("Hey, I am inside with")