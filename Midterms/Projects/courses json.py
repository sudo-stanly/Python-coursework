import re

subjects = [
    {
        "year_1_subjects" : {
            "bsit" : 
            {
                "1st_semester" : 
                {
                    "programming" : 0,
                    "introduction_to_computing" : 0
                }
            },
            "bscomsci" :
            {
                "1st_semester":
                {
                    "no available subjects" : None
                }
            }
        }
    }
]

list_of_subjects_for_student = []
list_of_grades_for_students = []

while True:
    try:
        x = int(input("[1] Enter , [2] Exit: "))

        year_level = 0
        if x != 2:
            
            print()
            
            """
            !-> important
                # year_dict = subjects[x - 1]
                # for year_level, courses in year_dict.items():
                #     print(f"\n[#] Courses available in {year_level}: ")

                #     course_list = list(courses.keys())
                #     for i, course in enumerate(course_list, start=1):
                #         print(f"[{i}] : {course}")

                #     y = int(input("Choose a course: "))
                #     chosen_course = course_list[y - 1]

                #     print(f"\n[#] Semesters in {chosen_course}:")
                #     semesters = courses[chosen_course]

                #     semester_list = list(semesters.keys())
                #     for j, sem in enumerate(semester_list, start=1):
                #         print(f"[{j}] : {sem}")

                #     z = int(input("Choose a semester: "))
                #     chosen_semester = semester_list[z - 1]

                #     print(f"\n[#] Subjects in {chosen_course} - {chosen_semester}: ")
                #     subjects_in_sem = semesters[chosen_semester]
                #     subject_list = list(subjects_in_sem.keys())
                #     for k, subj in enumerate(subject_list, start=1):
                #         print(f"[{k}] {subj}")
            """
            
            # instead of input, get input coming from student info. (instead of manual, it is auto filled)
            x = None
            x = 1 # example: 1st year
            year_chosen = subjects[x - 1]
        
            for year_level, courses in year_chosen.items():
                print(f"[#] Courses available in {year_level}")
                
                course_list = list(courses.keys())
                for i, course in enumerate(course_list, start=1):
                    print(f"[{i}] : {course}")
                
                y = 1 #example: bsit
                chosen_course = course_list[y - 1]
                
                print(f"\n[#] Semesters in {chosen_course}:")
                semesters = courses[chosen_course]

                semester_list = list(semesters.keys())
                for j, sem in enumerate(semester_list, start=1):
                    print(f"[{j}] : {sem}")
                    
                z = 1 # example: 1st sem
                chosen_semester = semester_list[z - 1]

                print(f"\n[#] Subjects in {chosen_course} - {chosen_semester}: ")
                subjects_in_sem = semesters[chosen_semester]
                subject_list = list(subjects_in_sem.keys())
                for k, subj in enumerate(subject_list, start=1):
                    print(f"[{k}] {subj}")
                    
            
            # user can then choose a subject for student.
            while True:
                
                user = int(input("Choose a subject: "))
                for year_level, courses in year_chosen.items():
                    
                    course_list = list(courses.keys())
                    y = 1
                    chosen_course = course_list[y - 1]
                    
                    semesters = courses[chosen_course]
                    semester_list = list(semesters.keys())
                    z = 1
                    chosen_semester = semester_list[z - 1]
            
                    semester_subjects = semesters[chosen_semester]
                    subject_list = list(semester_subjects.keys())

                    subject_index = user
                    chosen_subject = subject_list[user - 1]
                    
                    list_of_subjects_for_student.append(chosen_subject)
                    list_of_grades_for_students.append(semester_subjects[chosen_subject])
                    
                    print(f"subjects {list_of_subjects_for_student}")
                    print(f"grades {list_of_grades_for_students}")
                
        elif x == 2:
            break

 
    


    except Exception as e:
        print("\n[!] Invalid input\n")