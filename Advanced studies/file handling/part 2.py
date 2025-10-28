
#! SYNTAX

#* to open a file for reading it is enough to specify the name of the file:
f = open("./Advanced studies/file handling/demofile.txt")

#* The code above is the same as:
f = open("./Advanced studies/file handling/demofile.txt", "rt")
# because "r" for read, and "t" for text are the default values, you do not need to specify them.

#* Note: Make sure the file exists, or else you will get an error.