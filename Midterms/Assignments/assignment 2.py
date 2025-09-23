
#! assignment
#* create a simple grocery list using one of the collection discussed. It must accept an input from user.
#* User must be able to add and remove an item from the list.
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


list_of_products = ["White Potato", "Celery", "Cauliflower"]
list_of_groceries = []
count = 0

while True:
    try:
        user = int(input("[1] Enter , [2] Exit: "))
        if user == 1:
            clear()
            user = None
            
            while True:
                clear()
                
                print("--------------------------------------------------")
                print( str("FORBES COLLEGE GROCERY STORE").center(50))
                print("--------------------------------------------------")
                
                print()
                for products in list_of_products:
                    count += 1
                    print(f"{count}. {products}")
                    
                count = 0
                user = input("\n[#] (V) View list (Q) Quit program\n[!] Choose products to add : ")
                
                choice = []
                for char in user:
                    if char.isalpha():
                        choice.append(str(char).lower())
                        
                    if char.isdigit():
                        choice.append(int(char))
                
                if str(choice[0]).isdigit():
                    list_of_groceries.append(list_of_products[int(choice[0]) - 1])
                    
                else:
                    if str(choice[0]).isalpha():
                        if choice[0] == 'q':
                            clear()
                            list_of_groceries.clear()
                            print("[!] User has exited the program.")
                            break
                        elif choice[0] == 'v':
                            user = None
                            
                            while True:
                                clear()
                                
                                print("--------------------------------------------------")
                                print( str("GROCERY LIST").center(50))
                                print("--------------------------------------------------")
                                
                                if len(list_of_groceries) == 0:
                                    print("\n[!] Grocery list is empty.\n")
                                    
                                    user = int(input("[?] (0) Exit: "))
                                    if user == 0:
                                        break
                                else:
                                    #! count products in grocery list
                                    count = 0
                                    for element in list_of_products:
                                        count += 1
                                        count_grocery_product = list_of_groceries.count(element)
                                        
                                        if count_grocery_product != 0:
                                            print(f"{count}. {element} : (x{count_grocery_product})")
                                        
                                    count = 0
                                    print()
                                    user = input("[#] (Q) Edit Quantity (C) Clear (E) Exit\n[?] Choice: ")
                                
                                    choice = []
                                    for char in user:
                                        if char.isalpha():
                                            choice.append(str(char).lower())
                                            
                                        if char.isdigit():
                                            choice.append(int(char))
                                            
                                    if str(choice[0]).isdigit():
                                        clear()
                                        print("[!] Invalid input.")
                                        
                                    else:
                                        if str(choice[0]).isalpha():
                                            if choice[0] == 'e':
                                                clear()
                                                break
                                            elif choice[0] == 'q':
                                                user = None
                                                
                                                while True:
                                                    clear()
                                                    
                                                    print("--------------------------------------------------")
                                                    print( str("GROCERY LIST").center(50))
                                                    print("--------------------------------------------------")
                                                    
                                                    print()
                                                    count = 0
                                                    for element in list_of_products:
                                                        count += 1
                                                        count_grocery_product = list_of_groceries.count(element)
                                                        
                                                        if count_grocery_product != 0:
                                                            print(f"{count}. {element} : (x{count_grocery_product})")
                                                    
                                                    print()
                                                    product = int(input("[?] Choose a product to modify: ")) #* note: if input fails here, all existing list are saved, just enter and view again.
                                                    user = input("[#] (E) Exit\n[Modes]:\n\t(1) Add\n\t(2) Decrease\n[?] choice: ")
                                                    
                                                    choice = []
                                                    for char in user:
                                                        if char.isalpha():
                                                            choice.append(str(char).lower())
                                                            
                                                        if char.isdigit():
                                                            choice.append(int(char))
                                                    if str(choice[0]).isdigit():
                                                        print()
                                                        
                                                        if choice[0] == 1:
                                                            print()
                                                            
                                                            list_of_groceries.append(list_of_products[product - 1])
                                                            
                                                        elif choice[0] == 2:
                                                            print()
                                                            
                                                            list_of_groceries.remove(list_of_products[product - 1])
                                                            
                                                    else:
                                                        if choice[0] == 'e':
                                                            break
                                                        
                                            elif choice[0] == 'c':
                                                list_of_groceries.clear()
                
    
        elif user == 2:
            clear()
            print("[!] User has exited. Program is terminated")
            break
        
    except:
        clear()
        print("[!] Invalid input.")