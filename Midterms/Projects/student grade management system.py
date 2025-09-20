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

# def sumOfGrades(sub_grades):
#     result = 0
#     for x in sub_grades:
#         sub_grades += x
        
#     result = sub_grades
    
#     return result

while True:
    try:
        print("--------------------------------------------------")
        print( str("STUDENT GRADE MANAGEMENT SYSTEM").center(50))
        print("[1] Enter\n[2] Add-Edit-Delete Student/Course\n[3] List of students\n[4] Quit")
        print("--------------------------------------------------")
        option = int(input("[#] choice: "))
        
        if option == 1:
            clear()
            
            option = None
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
            available_courses = [
                "bachelor_of_science_in_information_technology", 
                "bsit", 
                
                "bachelor_of_computer_science", 
                "bscomsci"
            ]
            prepositions = ['of', 'in', 'the', 'on', 'at']
            
            
            while True:
                
                print("--------------------------------------------------")
                print( str("STUDENT GRADE MANAGEMENT SYSTEM").center(50))
                print("--------------------------------------------------")
            
                print()
                entered_name = input("[#] Name\t: ")
                entered_course = input("[#] Course\t: ")
                entered_year_level = input("[#] Year level\t: ")
                entered_semester = input("[#] Semester\t: ")
                
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
                    enrolled_student["course"] = " ".join(split_entered_course)
                    
                    # check if course name is abbreviated or full name and check if course is existant.
                    # print(f"entered course: {" ".join(split_entered_course)} : [{available_courses.count(" ".join(split_entered_course))}] found")

                    courses_available = available_courses.count("_".join(split_entered_course)) 
                    if courses_available == 0:
                        
                        while True:
                            clear()
                            
                            print("--------------------------------------------------")
                            print(str("COURSE NOT FOUND").center(50))
                            print("--------------------------------------------------")
                            
                            print()
                            print(f"[!] The course \"{entered_course.title()}\" is not in our list of\n    courses. You can add a course into the list\n    or exit this window.")
                            
                            option = input("\n[?] Do you wish to proceed? [Y] Yes , [N] No: ")
                            if option.lower() == 'y':
                                clear()
                                option = None
                                
                                while True:
                                    
                                    print("--------------------------------------------------")
                                    print(str("ADDING A COURSE").center(50))
                                    print("--------------------------------------------------")
                                    
                                    print()
                                    new_course = input("[#] Course name  : ")
                                    
                                    if len(new_course.split()) == 1:
                                        clear()
                                        
                                        print(f"[!] Please enter the full name of the course.")
                                        print()
                                        
                                    else:
                                        # abbreviate course name
                                        format_new_course = new_course.lower()
                                        remove_characters_from_new_course = re.sub(r"[,.!#$%^&*90@\d/?';:{}\-+=_]", "", new_course)
                                        split_course_name = remove_characters_from_new_course.split()
                                        list_course_name = list(split_course_name)
                                        
                                        #remove prepositions
                                        # prepositions = ['of', 'in', 'the', 'on', 'at']
                                        words_to_abbreviate = []
                                        for words in list_course_name:
                                            if words not in prepositions:
                                                words_to_abbreviate.append(words) 
                                
                                        abbreviations = []
                                        for x in range(len(words_to_abbreviate)):
                                            get_element = list(words_to_abbreviate[x])
                                            abbreviations.append(get_element[0].lower())
                                            
                                        print(f"[#] Abbreviation : ",end="")
                                        for x in abbreviations:
                                            print(str(x).upper(), end="")
                                    
                                        print("\n")
                                        print("[S] Submit , [C] Cancel")
                                        print("--------------------------------------------------")
                                        
                                        print()
                                        option = input("[#] Choice: ")
                                        if option.lower() == 's':
                                            clear()
                                            
                                            format_full_course_title = re.sub(r"\s", "_", new_course)
                                            # print(f"COURSE {format_full_course_title}")
                                            if available_courses.count(format_full_course_title) == 0:
                                            
                                                # title except prepositions
                                                format_course_title = new_course.split()
                                                list_of_formatted_course = list(format_course_title)
                                                
                                                print("[#] ' ", end="")
                                                for word in list_of_formatted_course:
                                                    if word not in prepositions:
                                                        print(word.title(), end=" ")
                                                        
                                                    if word in prepositions:
                                                        print(word.lower(), end=" ")
                                                    
                                                print("'",end=" ")   
                                                print("\n     course has been added to the list.",end="")
                                                
                                                
                                                # append abbreviated version
                                                #print("ABBREVIATIONS: ","".join(abbreviations))
                                                course_abbreviated = "".join(abbreviations)
                                                
                                                available_courses.append(format_full_course_title)
                                                available_courses.append(course_abbreviated)
                                                print()
                                                
                                                break
                                            else:
                                                clear()
                                                
                                                print("[!] Course is already in list, Please try another course.")
                                                print()
                                                
                                        elif option.lower() == 'c':
                                            clear()
                                            
                                            print("[!] Operation has been cancelled.")
                                            print()
                                            break
                                        
                                        
                            elif option.lower() == 'n':
                                clear()
                                option = None
                                    
                                while True:
                                    print("--------------------------------------------------")
                                    print(f"\n[!] Listing of course has been cancelled, you may\n    add \"{entered_course.title()}\" in the future.\n")
                                    print("--------------------------------------------------")

                                    option = input("[Q] Exit: ")
                                    if option.lower() == 'q':
                                        clear()
                                        option = None
                                        break
                                    else:
                                        clear()
                                        option = None
                                        print("[!] Invalid input.")
                            break

                    # year level
                    take_entered_year_level = str(entered_year_level).lower()
                    cleaned_entered_year_level = re.sub(r"[A-za-z,.!#$%^&*90@/?';:{}\-+=_]", "", take_entered_year_level)
                    if cleaned_entered_year_level:
                        enrolled_student["year_level"] = cleaned_entered_year_level
                    
                    else:
                        clear()
                        
                        print("[!] Year level must include a number.")
                        print()
                        
                    # semester
                    take_entered_semester = str(entered_semester).lower()
                    cleaned_entered_semester = re.sub(r"[A-za-z,.!#$%^&*90@/?';:{}\-+=_]", "", take_entered_semester)
                    if cleaned_entered_semester:
                        enrolled_student["semester"] = cleaned_entered_semester
                    
                    else:
                        clear()
                        
                        print("[!] Semester must include a number.")
                        print()
                        
                        
                    while True:
                        clear()
                        
                        option = None
                        print("--------------------------------------------------")
                        print( str("STUDENTS INFORMATION").center(50))
                        print("--------------------------------------------------")
                        
                        print()
                        print(f"[#] Name\t: {enrolled_student["name"]}")
                        
                        print("[#] Course\t: ", end="")
                        e_course = enrolled_student["course"].split(" ")
                        list_e_course = list(e_course)
                        # print(f"{list_e_course} : length : {len(list_e_course)}")
                        #! todo
                        if len(list_e_course) == 1:
                            print(" ".join(list_e_course).capitalize())
                                
                            print()                           
                            option = input(":")
                        else:
                            for words in list_e_course:
                                if words not in prepositions:
                                    print(words.title(), end=" ")
                                if words in prepositions:
                                    print(words.lower(), end=" ") 
                            
                            print()                           
                            option = input(":")
                else:
                    clear()
                    print("[!] Field/s cannot be empty.")
        
        elif option == 4:
            clear()
            print("\n[-] Program ended.\n")
            
            break
                
    except:
        clear()
        print("[!] Invalid input.\n")