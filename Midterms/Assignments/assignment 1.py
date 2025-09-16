"""
    ! Student Grade Management System

    *Create a simple grade management system for a teacher. The system should be able to calculate grades. At least 3 functions.
        * -> Example function.
        * -> FUNCTION 1: Calculate average
        * -> FUNCTION 2: Letter grade
        * -> FUNCTION 3: Grade status
"""

#* function with parameters
#*  -> get user input
#*  -> hmm... subjects?
#*  -> looped
#*  -> assign a sequence?
#*  -> option first?
#*  -> how many subjects?
#*  -> store them in a sequence (list)
#*  -> name of student?
#*  -> then functions (pass the list into the function)

#*  -> validate for empty grade

#! calculate average: sum of all subject grades divided by number of subjects.
#! letter grade depending on grade.
#! grade status, pass, fail
#! hmmm... 

#! course?

list_of_subjects = []
list_of_grades = []
student = ""
students_course = ""
number_of_subjects = 0
final_grade = 0
GPA = ""
   
def calculateAverage():

    while True:
        try:
            option = int(input("[1] Evaluate Grades [2] Quit: "))
            
            if option == 1:
                
                print()
                course_of_student = input("[?] Course of student: ")
                students_course = course_of_student

                name_of_student = input("[?] Name of student: ")
                student = name_of_student
                
                while True:
                    
                    system = int(input("[?] How many subjects to enter? "))
                    number_of_subjects = system
                    
                    print()
                    for x in range(system):
                        subjects = input("[!] Please enter your subject/s: ")
                        list_of_subjects.append(subjects)
                        
                    print()
                    system_grade = system
                    for x in range(system_grade):
                        grades = int(input(f"[!] Enter grade for this subject ({list_of_subjects[x]}): "))
                        list_of_grades.append(grades)
                        
                    print()
                    
                    x = list_of_subjects.count("")
                    y = list_of_grades.count("")
                    
                    if x == 0 and y == 0:
                        
                        #! print(f"GRADES: {list_of_grades}")
                        sum_of_grades = 0
                        for i in list_of_grades:
                            sum_of_grades += i
                        #! print(f"SUM OF GRADES IS {sum_of_grades}")
                        
                        evaluation_of_grade = sum_of_grades / number_of_subjects
                        final_grade = evaluation_of_grade
                        
                        #* print(f"The final grade of {student} is {evaluation_of_grade:.1f}")
                        print("--------------------------------------------------")
                        print(f"\nCOURSE\t\t: {students_course.upper()}")
                        print(f"NAME\t\t: {student.title()}\nGRADE\t\t: {evaluation_of_grade:.1f}")
                        
                        letterGrade(final_grade)
                        
                        break
                    else:               
                        if x > 0 and y > 0:
                            print("[!] Missing subject/s and grade/s. Please try again.") 
                            list_of_subjects.clear()
                            list_of_grades.clear()
                            
                        elif x > 0 and y == 0:
                            print("[!] Missing subject/s with complete grade. Please try again.")   
                            list_of_subjects.clear()
                            list_of_grades.clear()
                            
                        elif x == 0 and y > 0:
                            print("[!] Incomplete grade/s with complete subjects. Please try again.")   
                            list_of_subjects.clear()
                            list_of_grades.clear()     
                    print()
                
            elif option == 2:
                break
            
        except:
            print(" [!] Invalid input")
            
def letterGrade(f_grade):

    evaluated_grade = int(f_grade)
    print(f"FINAL GRADE\t: {evaluated_grade}")
    
    print()
    if evaluated_grade >= 95 and evaluated_grade <= 100:
        print("REMARKS\t\t: A\nGPA\t\t: 1")
        GPA = "1"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 90 and evaluated_grade <= 95:
        print("REMARKS\t\t: A\nGPA\t\t: 1.5")
        GPA = "1.5"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 85 and evaluated_grade <= 90:
        print("REMARKS\t\t: B\nGPA\t\t: 2")
        GPA = "2"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 80 and evaluated_grade <= 85:
        print("REMARKS\t\t: B\nGPA\t\t: 2.5")
        GPA = "2.5"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 75 and evaluated_grade <= 80:
        print("REMARKS\t\t: C\nGPA\t\t: 3")
        GPA = "3"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 70 and evaluated_grade <= 75:
        print("REMARKS\t\t: D\nGPA\t\t: 3.5")
        GPA = "3.5"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 65 and evaluated_grade <= 70:
        print("REMARKS\t\t: F\nGPA\t\t: 4")
        GPA = "4"
        gradeStatus(GPA)
        print()
        
    elif evaluated_grade >= 0 and evaluated_grade <= 65:
        print("REMARKS\t\t: F\nGPA\t\t: 4.5")
        GPA = "4.5"
        gradeStatus(GPA)
        print()
        
def gradeStatus(stats):

    if stats == "1":
        print("STATUS\t\t: Passed")
        
    elif stats == "2":
        print("STATUS\t\t: Passed")
        
    elif stats == "2.5":
        print("STATUS\t\t: Passed")
        
    elif stats == "3":
        print("STATUS\t\t: Passed")
        
    elif stats == "3.5":
        print("STATUS\t\t: Inc")
        
    elif stats == "4":
        print("STATUS\t\t: Inc")

    elif stats == "4.5":
        print("STATUS\t\t: Failed")
        
    print()
    print("--------------------------------------------------")
    
    list_of_subjects.clear()
    list_of_grades.clear()
    student = ""
    students_course = ""
    number_of_subjects = 0
    final_grade = 0
    GPA = ""
        
calculateAverage()