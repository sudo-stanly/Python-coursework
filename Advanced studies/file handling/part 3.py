
#! PYTHON OPEN FILE

#* Open a file on the server
# assume we have the following file, located in the same folder as Python
"""
    Hello! Welcome to demofile.txt
    This file is for testing purposes.
    Good Luck!
"""

"""
    To open the file, use the built-in open() function.
    The open() function returns a file object, which has a read() method for reading the content of the file:
"""
# example
f = open("./Advanced studies/file handling/demofile.txt")
print(f.read())


#* If the file is located in a different location, you will have to specify the file path, like this:
#Example
# Open a file on a different location:

#! windows
#*  f = open("D:\\myfiles\welcome.txt")
#*  print(f.read())

#f = open("C:\Users\Your name\Directory\filename.txt")
# f = open("C:\Users\Name\Documents\file.txt")

#! linux
#f = open("/home/name/directory/filename.txt")
# f = open("/home/aspire/Downloads/demofile.txt")
# print(f.read())



#! USING THE 'with' statement
#example
# using the 'with' keyword:
with open("./Advanced studies/file handling/demofile.txt") as f:
    print(f.read())
