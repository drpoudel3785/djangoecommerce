"""
f = open(filename, mode)
Where the following mode is supported:
1.	r: open an existing file for a read operation.
2.	w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
3.	a:  open an existing file for append operation. It won’t override existing data.
4.	 r+:  To read and write data into the file. The previous data in the file will be overridden.
5.	w+: To write and read data. It will override existing data.
6.	a+: To append and read data from the file. It won’t override existing data.

"""
import os
#This method returns the current working directory in the form of a string
print(os.getcwd())

print("===================")

# We can change the current working directory by using the chdir() method
#os.chdir('D:\\CLASS')
#print(os.getcwd())
#All files and sub-directories inside a directory can be retrieved using the listdir() method.
print(os.listdir())
print("===================")
print(os.listdir('D:\\'))
#We can make a new directory using the mkdir() method.
# Check if a File or Directory Exists in Python using os.path.isfile()
folder="test"
if os.path.isdir(folder):
    print ("Folder already Exist")
else:
    os.mkdir('test')
#renaming the directory
if os.path.isdir("test"):
    if os.path.isdir("new_one"):
        print("Sorry new One alreasy Exist")
    else:
        os.rename('test', 'new_one')
else:
    print("Sorry No test folder exist")

 #A file can be removed (deleted) using the remove() method.
#Similarly, the rmdir() method removes an empty directory.


# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)
# Python code to illustrate read() mode
file = open('geek.txt', 'r')
print (file.read())


# Python code to illustrate read() mode character wise
file = open("geek.txt", "r")
print (file.read(5))


file = open('geek.txt','a+')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
print("-----------------------")

# Python code to illustrate with()
with open("geek.txt") as file:
    data = file.read()
# do something with data
    print (data)
print("------------------")
"""We can also split lines using file handling in Python. This splits the variable when space is encountered. You can also split using any characters as we wish. Here is the code:"""
with open("geek.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

