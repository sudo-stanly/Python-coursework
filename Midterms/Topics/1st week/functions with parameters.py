
#* fstring
def fString(name):
    print(f"my name is {name}")
fString("Stan")

#! create a function with parameters of name and age and check if age is odd or even.
def logFunc(name, age):
        
        print(f"my name is {name} i am {age} years old")
        
        if age % 2 == 0:
            print(f"{age} is even")
        else:
            print(f"{age} is odd")
logFunc("Stan", 20)
    
    
    
#* what if (with birthyear and current date)
def ageFunc(**user):
    
    if user["currentYear"] > user["birthYear"]:
        age = int(user["currentYear"]) - int(user["birthYear"])
        print(f"My name is {user["name"]} i am {age} years old.")
    
        if age % 2 == 0:
            print(f"{age} is even.")
        else:
            print(f"{age} is even.")
    else:
        age = int(user["birthYear"]) - int(user["currentYear"])
        print(f"My name is {user["name"]} i am {age} years old.")
    
        if age % 2 == 0:
            print(f"{age} is even.")
        else:
            print(f"{age} is even.")
ageFunc(name = "Stan", currentYear = 2025, birthYear = 3200)