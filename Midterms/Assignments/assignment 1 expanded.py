import re
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

"""

    ! STUDENT GRAED MANAGEMENT SYSTEM:
    * -> assignment 1 expanded version
    * -> store students/grades/course/year level/gpa/grade status in an object
    * -> create a function that evaluates the grade and function for the grade status and letter grade

"""

students = [
    {
        "name"         : [],
        "course"       : "",
        "year_level"   : "",
        "semester"     : "",
        "final_grade"  : float(0),
        "letter_grade" : "",
        "gpa"          : float(0),
        "grade_status" : "",
    }
]

def sumOfGrades(sub_grades):
    result = 0
    for x in sub_grades:
        sub_grades += x
        
    result = sub_grades
    
    return result

while True:
    try:
        option = int(input("[1] Enter, [2] Search, [3] Quit: "))
        
        if option == 1:
            clear()
            
            enrolled_student = {
                    "name"         : [],
                    "course"       : "",
                    "year_level"   : int(0),
                    "semester"     : int(0), 
                    "final_grade"  : float(0),
                    "letter_grade" : "",
                    "gpa"          : float(0),
                    "grade_status" : "",
            }
            courses = {
                "bachelor_of_science_in_information_technology" : "bsit".upper(),
                "bsit" : "bsit".upper(),
                "bachelor_of_computer_science" : "comsci".upper(),
                "comsci" : "comsci".upper()
            }
            
            while True:
                
                print("--------------------------------------------------")
                opt = str("STUDENT GRADE MANAGEMENT SYSTEM").center(50)
                print(opt)
                print("--------------------------------------------------")
            
                print()
                entered_name = input("[?] Name\t: ")
                entered_course = input("[?] Course\t: ")
                entered_year_level = input("[?] Year level\t: ")
                entered_semester = input("[?] Semester\t: ")
                
                if entered_name != "" and entered_course != "" and entered_year_level != "" and entered_semester != "":
                    clear()
                    
                    # name
                    take_entered_name = str(entered_name).lower().title()
                    cleaned_entered_name = re.sub(r"[,.!#$%^&*90@\d/?';:{}\-+=_]", "", take_entered_name)
                    split_entered_name = str(cleaned_entered_name).split()
                    enrolled_student["name"] = " ".join(split_entered_name)
                    
                    # course
                    take_entered_course = str(entered_course).lower()
                    cleaned_entered_course = re.sub(r"[,.!#$%^&*90@\d/?';:{}\-+=_]", "", take_entered_course)
                    split_entered_course = str(cleaned_entered_course).split()
                    
                    # check if course name is abbreviated or full name
                    if len(split_entered_course) == 1:
                        enrolled_student["course"] = " ".join(split_entered_course).lower()
                        for key, value in courses.items():
                            if enrolled_student["course"] == key:
                                enrolled_student["course"] = value
                                
                            elif enrolled_student["course"] != key:
               
                                while True:
                                    clear()
                                                                    
                                    enrolled_student["name"] = ""
                                    enrolled_student["course"] = ""
                                    enrolled_student["year_level"] = 0
                                    enrolled_student["semester"] = 0
                                    
                                    print("--------------------------------------------------")
                                    opt = str("COURSE NOT FOUND").center(50)
                                    print(opt)
                                    print(str("[E] Exit, [A] Add course").center(50))
                                    print("--------------------------------------------------")
                                    
                                    print()
                                    print(f"[!] \"{entered_course.title()}\" course is not available,\n     please check the list of available courses.\n")
                                    
                                    course_list = []
                                    for key, value in courses.items():
                                        course_list.append(key)
                                        
                                    for i in range(0, len(course_list), 2):
                                        formatted_course_list = str(course_list[i]).replace('_', ' ')
                                        print(f"* {formatted_course_list}")

                                    print()
                                    course_option = input("[?] Choice: ")
                                    
                                    if course_option.lower() == 'a':
                                        course_option = None
                                        clear()
                                        
                                        print("--------------------------------------------------")
                                        opt = str("ADDING A COURSE").center(50)
                                        print(opt)
                                        print("--------------------------------------------------")
                                        
                                        print()
                                        new_course = input("[?] Full name of course: ")
                                        
                                        # convert an abbreviation
                                        split_course_title = new_course.lower().split()
                                        
                                        if "of" in split_course_title:
                                            split_course_title.remove("of")
                                            
                                        if "in" in split_course_title:  
                                            split_course_title.remove("in")
                                            
                                        if "the" in split_course_title:
                                            split_course_title.remove("the")
                                            
                                        if "or" in split_course_title:
                                            split_course_title.remove("or")
                                            
                                        if "on" in split_course_title:
                                            split_course_title.remove("or")
                                        
                                        abbreviation_of_the_course = []
                                        for x in range(len(split_course_title)):
                                            get_element = list(split_course_title[x])
                                            abbreviation_of_the_course.append(get_element[0].upper())
                                            
                                        print(f"[+] Abbreviation: ",end="")
                                        for x in abbreviation_of_the_course:
                                            print(x, end="")
                                        
                                        print()
                                        while True:
                                            course_option = input("[?] Press 'C' to cancel, 'S' to save: ")
                                            
                                            if course_option.lower() == 'c':
                                                clear()
                                                print("[!] Course has been cancelled.")
                                                break
                                            
                                            elif course_option.lower() == 's':
                                                clear()
                                                print("[!] Course has been saved.")
                                                break
                                               
                                                
                                            else:
                                                print("[!] Invalid input.")
                                            
            
                                    else:
                                        clear()
                                        print("[!] Exited.")
                                        
                                        break
                                     
                    else:
                        enrolled_student["course"] = "_".join(split_entered_course).lower()
                        
                        for key, value in courses.items():
                            if enrolled_student["course"] == key:
                                enrolled_student["course"] = value
                            elif enrolled_student["course"] != key:
                                clear()
                                enrolled_student["name"] = ""
                                enrolled_student["course"] = ""
                                enrolled_student["year_level"] = 0
                                enrolled_student["semester"] = 0
                                
                                print("No course found.")
                                
                                course_list = []
                                for key, value in courses:
                                    course_list.append(" ".join(key))
                                    
                                for i in range(0, len(course_list), 2):
                                    print(course_list[i], end = " ")
                                

                    # year level
                    take_entered_year_level = str(entered_year_level).lower()
                    cleaned_entered_year_level = re.sub(r"[A-za-z,.!#$%^&*90@/?';:{}\-+=_]", "", take_entered_year_level)
                    if cleaned_entered_year_level:
                        enrolled_student["year_level"] = cleaned_entered_year_level
                        
                        #print(enrolled_student)
                        
                    else:
                        clear()
                        print("[!] Year level must be a number.")
                    
                else:
                    clear()
                    print("[!] Field/s cannot be empty.")
        
        elif option == 3:
            clear()
            print("[-] Program ended.")
            
            break
                
    except:
        clear()
        print("[!] Invalid input.\n")