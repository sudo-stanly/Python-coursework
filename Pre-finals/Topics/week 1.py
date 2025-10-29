
#! FILE HANDLING
# file handling lets your program store data permanently - unlike variables, which are temporary
# and disappear whe nthe program stops running.
# its ysed to read/write files such as .txt, .cssv, .json, etc.

#* common modes
#!      MODE                MEANING
#*      "r"                 Read
#*      "w"                 Write
#*      "a"                 Append


#! OPENING A FILE
# to open a file, use Python's built-in open() function

#! Syntax
# open("filename", "mode") #* open("sample.txt", "r")

# depending where the file is, it must be in the same directory if not, apply drectory './directory/filename'


#! 2. READING FROM A FILE
# let's say sample.txt contains
#   Hello world!
#   Welcome to Python file handling.

#* METHOD 1: Read entire file
file = open("./Pre-finals/Topics/sample.txt", "r")
print(file.read())
file.close()


#* METHOD 2: Read only first 10 characters
file = open("./Pre-finals/Topics/sample.txt", "r")
print(file.read(10))
file.close()


#* METHOD 3: Read line by line
file = open("./Pre-finals/Topics/sample.txt", "r")
print(file.readline()) # Reads first line
print(file.readline()) # Reads second line
file.close()

#* Read line by line using for loop
file = open("./Pre-finals/Topics/sample.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip()) # .strip() removes newline
file.close()


#* returning text as list and removing '\n' by stripping
notes = []  
with open("./Pre-finals/Topics/sample.txt", "r") as file:
    for line in file.readlines():
        if line.strip():              
            notes.append(line.strip())
print(notes)


#! 3. WRITING TO A FILE
# example:

#* Overwriting the file
file = open("./Pre-finals/Topics/sample.txt", "w")
file.write("this will overwrite the existing content.")
file.close()

#* Appending data (without erasing):
file = open("./Pre-finals/Topics/sample.txt", "a")
file.write("\nThis line was appended.")
file.close()


#! 4. CLOSING FILES
# always close files after using them:
file.close()

#* or better, use with statement - it auto closes the file:
with open("./Pre-finals/Topics/sample.txt", "r") as file:
    data = file.read()
    print(data)
    

#! 5. READ AND WRITING TOGETHER
# you can also read and write:

with open("./Pre-finals/Topics/sample.txt", "r+") as file:
    content = file.read()
    file.write("\nExtra content added!")
    


#! CHECKING IF A FILE EXISTS
# use the os module:

import os 
if os.path.exists("./Pre-finals/Topics/sample.txt"): #! for directory -> ("./Directory/Folder/filename")
    print("File exists!")
else:
    print("File not found!")
    
    
#! DELETING A FILE
# we also use the os module for deleting a file:
os.remove("./Pre-finals/Topics/sample.txt")

#* always check first before deleting
if os.path.exists("./Pre-finals/Topics/sample.txt"): #! for directory -> ("./Directory/Folder/filename")
    os.remove("./Pre-finals/Topics/sample.txt")
else:
    print("File not found!")
            

#! CREATING A FILE
# check first if file exists

if os.path.exists("./Pre-finals/Topics/sample.txt"): #! for directory -> ("./Directory/Folder/filename")
    print("File exists!")
else:
    with open("filename", "x") as file:
        print("File created!")
        
        
        
#! 8. BONUS: WORKING WITH CSV OR JSON

#* CSV
import csv

# Writing
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Kokoy', 25])

# Reading
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
        
#* JSON
import json
data = {"name": "Kokoy", "role": "Full Stack Developer"}

# Write
with open("data.json", "w") as f:
    json.dump(data, f)

# Read
with open("data.json", "r") as f:
    result = json.load(f)
    print(result)
    
    


#! PRACTICE
    #* Practice Exercise
    # Create a text file students.txt
    # Write 3 names in it
    # Read the file and print each line
    # Append a new name
    # Print the final file contents
    
 # 1. Create a text file and write 3 names in it
with open("students.txt", "w") as f:
    f.write("Kokoy\n")
    f.write("John Doe\n")
    f.write("Alex Gonzaga\n")

# 2. Read the file and print each line
with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())

# 3. Append a new name
with open("students.txt", "a") as f:
    f.write("Elon\n")

# 4. Print the final file contents
with open("students.txt", "r") as f:
    print("\nFinal file contents:")
    print(f.read())
