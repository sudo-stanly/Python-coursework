import re
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

school = [
    {
        "1st_year" :{
            "bsit" : {
                "1st_semester" : {
                    "programming_1" : 0,
                    "introduction_to_computing" : 0,
                    "visual_arts_and_crafts" : 0,
                    "nstp_1_cwts" : 0,
                },
                "2nd_semester" : {
                    "programming_2" : 0,
                    "principles_of_accounting" : 0,
                    "web_system_and_technologies" : 0,
                }
            }
        },
        "2nd_year" :{
            "bsit" : {
                "1st_semester" : {
                    "gender_and_society" : 0,
                    "understanding_the_self" : 0,
                    "event_driven_programming" : 0,
                    "integrative_programming_1" : 0,
                    "object_oriented_programming" : 0,
                    "human_computer_interaction" : 0,
                },
                "2nd_semester" : {
                    "data_structures_and_algorithm" : 0,
                    "platform_technologies" : 0,
                    "discrete_mathematics" : 0,
                    "living_in_the_it_era" : 0,
                    "purposive_communication" : 0,
                    "integrative_programming_2" : 0,
                    "advanced_database_management_system" : 0
                }
            }
        },
        "3rd_year" :{
            "bsit" : {
                "1st_semester" : {
                    "app_development" : 0,
                    "python_programming" : 0,
                    "system_analysis_and_design" : 0,
                    "mathematics_in_the_modern_world" : 0,
                    "networking_1" : 0,
                    "information_assurance" : 0,
                    "quantitatve_methods" : 0
                },
                "2nd_semester" : {
                   "message" : "[!] Subjects of this semester is soon to be announced."
                }
            }
        },
        "4th_year" :{
            "bsit" : {
                "1st_semester" : {
                    "message" : "[!] Subjects of this semester is soon to be announced."
                },
                "2nd_semester" : {
                   "message" : "[!] Subjects of this semester is soon to be announced."
                }
            }
        }
    }
]


user = None
choice = []

year_level = None
semester = None
    
clear()
while True:
    try:
        print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'))
        user = int(input("\nPress 1 to enter, 0 to exit: ".rjust(5)))
        
        if user == 1:
            clear()
            
            while True:
                print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(ROLES)".center(50), "\n\n* As Deans your role is to view, add, and remove\n  subjects.".rjust(5), "\n\n* As Instructor your role is to grade the subject\n  and students.".rjust(5), "\n")
                user = input("Press 'C' to continue, 'R' to return: ")
                if user.lower() == 'c':
                    clear()
                    user = None
                    
                    while True:
                        print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(SUBJECTS)".center(50), "\n\n* Choosing Deans means you can view, add, and\n  remove a subject from a specific department.".rjust(5), "\n")
                        user = input("Press 'C' to continue, 'R' to return: ")
                        if user.lower() == 'c':
                            clear()
                            user = None
                            
                            while True:
                                print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(STUDENTS)".center(50), "\n\n* Choosing Instructor means you must list\n  regular students and irregular students for\n  proper subject grading.".rjust(5), "\n")
                                user = input("Press 'C' to continue, 'R' to return: ")
                                
                                if user.lower() == 'c':
                                    clear()
                                    user = None
                                    
                                    while True:
                                        print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(ROLES)".center(50), "\n\n  [1] Deans\n  [2] Instructor".rjust(5), "\n")
                                        user = input("Enter the role of your choice or press 'R' to\nreturn: ")
                                        for char in user:
                                            if str(user).isalpha():
                                                choice.append(str(char).lower())
                                            if str(user).isdigit():
                                                choice.append(int(char))
                                                
                                        if str(choice[0]).isdigit():
                                            if int(choice[0]) == 1: #! ROLE (DEANS) condition
                                                clear()
                                                user = None
                                                choice = []
                                                
                                                while True:
                                                    print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(DEANS)".center(50), "\n\n* Choose your department:\n  [1] IT Department".rjust(5), "\n")
                                                    user = input("Enter the department of your choice or press 'R'\nto return: ")
                                                    for char in user:
                                                        if str(user).isalpha():
                                                            choice.append(str(char).lower())
                                                        if str(user).isdigit():
                                                            choice.append(int(char))
                                                            
                                                    if str(choice[0]).isdigit(): #! IT DEPARTMENT (Deans) condition
                                                        if int(choice[0]) == 1:
                                                            clear()
                                                            user = None
                                                            choice = []
                                                                
                                                            while True:
                                                                print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(DEANS)".center(50), "\n\n* Choose courses related to IT:\n  [1] Information Technology".rjust(5), "\n")
                                                                user = input("Enter the department of your choice or press 'R'\nto return: ")
                                                                for char in user:
                                                                    if str(user).isalpha():
                                                                        choice.append(str(char).lower())
                                                                    if str(user).isdigit():
                                                                        choice.append(int(char))
                                                                        
                                                                if str(choice[0]).isdigit():
                                                                        if int(choice[0]) == 1:
                                                                            clear()
                                                                            user = None
                                                                            choice = []
                                                                            
                                                                            while True:
                                                                                print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(DEANS IT DEPT.)".center(50), "\n\n* Choose a mode:\n  [1] View subject/s\n  [2] Add subject/s\n  [3] Remove subjects/s".rjust(5), "\n")
                                                                                user = input("Enter a mode or press 'R' to return: ")
                                                                                for char in user:
                                                                                    if str(user).isalpha():
                                                                                        choice.append(str(char).lower())
                                                                                    if str(user).isdigit():
                                                                                        choice.append(int(char))
                                                                                if str(choice[0]).isdigit():
                                                                                    if int(choice[0]) == 1: #! VIEW MODE
                                                                                        clear()
                                                                                        user = None
                                                                                        choice = []
                                                                                        
                                                                                        while True:
                                                                                            try:
                                                                                                print(" STUDENT GRADE MANAGEMENT SYSTEM ".center(50,'*'),"\n","(DEANS IT DEPT.)".center(50), "\n\n* Choose a year level:\n  [1] 1st year\n  [2] 2nd year\n  [3] 3rd year\n  [4] 4th year".rjust(5))
                                                                                                year_level = int(input("  Enter year level: "))
                                                                                                
                                                                                                print("\n* Choose semester:\n  [1] 1st sem\n  [2] 2nd sem".rjust(5))
                                                                                                semester = int(input("  Enter semester: "))
                                                                                                
                                                                                                
                                                                                            except:
                                                                                                clear()
                                                                                                print("[ ! ] Invalid input. Please enter a number [ ! ]".center(50))
                                                                                            
                                                                                        
                                                                                    elif int(choice[0]) == 2: #! ADD MODE
                                                                                        print()
                                                                                    elif int(choice[0]) == 3: #! REMOVE MODE
                                                                                        print()
                                                                                    else:
                                                                                        clear()
                                                                                        user = None
                                                                                        choice = []
                                                                                        print("[ ! ] Invalid input [ ! ]".center(50))
                                                                                        
                                                                                else:
                                                                                    if str(choice[0]).isalpha():
                                                                                        if str(choice[0]) == 'r':
                                                                                            clear()
                                                                                            user = None
                                                                                            choice = []
                                                                                            break
                                                                                        else:
                                                                                            clear()
                                                                                            user = None
                                                                                            choice = []
                                                                                            print("[ ! ] Invalid input [ ! ]".center(50))
                                                                else:
                                                                    if str(choice[0]).isalpha():
                                                                        if str(choice[0]) == 'r':
                                                                            clear()
                                                                            user = None
                                                                            choice = []
                                                                            break
                                                                        else:
                                                                            clear()
                                                                            choice = []
                                                                            print("[ ! ] Invalid input [ ! ]".center(50))
                                                    else:
                                                        if str(choice[0]).isalpha():
                                                            if str(choice[0]) == 'r':
                                                                clear()
                                                                user = None
                                                                choice = []
                                                                break
                                                            else:
                                                                clear()
                                                                user = None
                                                                choice = []
                                                                print("[ ! ] Invalid input [ ! ]".center(50))
                                                
                                            elif int(choice[0]) == 2: #! ROLE (INSTRUCTOR) condition
                                                print()
                                                
                                            else:
                                                clear()
                                                user = None
                                                choice = []
                                                print("[ ! ] Invalid input [ ! ]".center(50))
                                                
                                        else:
                                            if str(choice[0]).isalpha():
                                                if str(choice[0]) == 'r':
                                                    clear()
                                                    user = None
                                                    choice = []
                                                    break
                                                else:
                                                    clear()
                                                    user = None
                                                    choice = []
                                                    print("[ ! ] Invalid input [ ! ]".center(50))
                                    
                                elif user.lower() == 'r':
                                    clear()
                                    user = None
                                    break
                                else:
                                    clear()
                                    print("[ ! ] Invalid input [ ! ]".center(50))
                            
                        elif user.lower() == 'r':
                            clear()
                            user = None
                            break
                        else:
                            clear()
                            print("[ ! ] Invalid input [ ! ]".center(50))
                    
                elif user.lower() == 'r':
                    clear()
                    user = None
                    break
                else:
                    clear()
                    print("[ ! ] Invalid input [ ! ]".center(50))
                        
        elif user == 0:
            clear()
            print(" PROGRAM HAS ENDED ".center(50,'*'))
            break
    except:
        clear()
        print("[ ! ] Invalid input [ ! ]".center(50))
        