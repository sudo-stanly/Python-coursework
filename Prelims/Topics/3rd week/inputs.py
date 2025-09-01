import math

#* =============================================
#* TOPIC : User Input
#* =============================================

"""

    * User input:
    ! Python allows for user input. That means we are able to ask the user for input
    ! for example the program asks for your name and when you enter a name it gets
    ! printed on the screen.

"""

#! examples:

#* Ask for user input:
#print("Enter your name:")
#name = input()
#print(f"Hello {name}")

#* you can change the type of the input like number
# try:
#     prompt = int(input("Choose a number 1 - 10:"))
#     print(f"Prompted\t: {prompt}")
# except:
#     print("\033[1;91m[!] Invalid Prompt :\033[0m \033[1;93mPlease choose a number!\033[0m")
    
    
#* you can also find the square root of a number
# try:
#     prompt = int(input("Enter a number:"))
#     print(f"Square root of {prompt} is : {math.sqrt(prompt)}")
# except:
#     print("\033[1;91m[!] Invalid Prompt :\033[0m \033[1;93mPlease enter a number!\033[0m")
    
    
#* it is also important to validate inputs
try:
    isActive = True
    while isActive:
        prompt = int(input("\nEnter a number [1] Enter, [0] Exit:"))
        
        if prompt == 1:
            prompt = None
            prompt = int(input("Enter a number: "))
            print(f"Square root of {prompt} is : {math.sqrt(prompt)}")
            
        elif prompt == 0:
            prompt = None
            print("\033[1;93mGoodbye!\033")
            break 
except:
    print("\033[1;91m[!] Invalid Prompt :\033[0m \033[1;93mPlease enter a valid number.\033[0m")
