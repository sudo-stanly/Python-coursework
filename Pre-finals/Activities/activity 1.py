
import os

if os.path.exists("./Pre-finals/Activities/students.txt"):
    
    list_of_names = ["Linus Torvalds\n", "Charles Babbage\n", "Van Rossum\n"]
    with open("./Pre-finals/Activities/students.txt", "w") as f:
        for i in list_of_names:
            f.write(i)
        
    with open("./Pre-finals/Activities/students.txt", "r") as f2:
        lines = f2.readlines()
        for line in lines:
            print(line.strip())

    with open("./Pre-finals/Activities/students.txt", "a") as f3:
        student = "Stanley Alerta"
        f3.write(student)
        
    with open("./Pre-finals/Activities/students.txt", "r") as f4:
        print(f4.read())
    
    
else:
    with open("./Pre-finals/Activities/students.txt", "x") as f:
        print("file does not exist, file has been created.\n run program again.")