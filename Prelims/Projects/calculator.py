
#* Simple Calculator Project: 
import time
try:
    prompt = int(input("\033[1;93m [*] CHOICES [1]-Enter [0]-Exit: \033 \033[0m"))
    # print(f"prompt: {prompt}")
    if prompt == 1:
        isActive = True
        while isActive:
            prompt = None
            print("\n\033[1;93m WRITE AN ARITHMETIC OPERATION: value + value, etc...")
            prompt = input("\033[0m [ +, -, *, / ] Enter your operation (num1, operator, num2): ")
            x = prompt.split()

            if len(x) > 3:
                for c in "\033[1;91m [!] Invalid Input.": print(c, end="", flush=True) or time.sleep(0.05)
                print("\n")
            else:
                match(x[1]):
                    case "+":
                        print(f" Sum of x is: {int(x[0]) + int(x[2])}")
                        
                    case "-":
                        print(f" Difference of x is: {int(x[0]) - int(x[2])}")
                        
                    case "*":
                        print(f" Product of x is: {int(x[0]) * int(x[2])}")
                        
                    case "/":
                        print(f" Quotient of x is  : {int(x[0]) / int(x[2])}")
                        print(f" Remaining of x is : {int(x[0]) % int(x[2])}")
                            
                    case _:
                        for c in "\033[1;91m [!] Invalid Input, \033[1;93mOperation failed.\033": print(c, end="", flush=True) or time.sleep(0.05)
                        print(" ")
    elif prompt == 0:
        for c in "\033[1;93m Goodbye!\033": print(c, end="", flush=True) or time.sleep(0.05)
        print("\n")
except:
    for c in "\033[1;91m [!] Invalid Input, \033[1;93mPlease try again!\033": print(c, end="", flush=True) or time.sleep(0.05)
    print("\n")