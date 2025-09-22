
#* -> testing access

# subjects = [
#     {
#         "year_1_subjects" : {
#             "1st_semester" : {
#                 "programming" : {
#                     "prelims" : 0,
#                     "midterms" : 0,
#                     "prefinals" : 0,
#                     "finals" : 0
#                 },
#                 "introduction_to_computing" : {
#                     "prelims" : 0,
#                     "midterms" : 0,
#                     "prefinals" : 0,
#                     "finals" : 0
#                 }
#             }
#         }
#     }
# ]
# print(subjects[0]["year_1_subjects"]["1st_semester"])

#! important!
# for year_level, semesters in subjects[0].items():
#     print(year_level)
    
#     for semester, subjects in semesters.items():
#         print(semester)
        
#         for subjects, grades in subjects.items():
#             print(subjects, end=" ")
            
#             for subject_grade, grade in grades.items():
#                 print(grade, end=" ")


#*


# subjects = [
#     {
#         "year_1_subjects" : {
#             "bsit" : 
#             {
#                 "1st_semester" : 
#                 {
#                     "programming" : {
#                         "prelims" : 0,
#                         "midterms" : 0,
#                         "prefinals" : 0,
#                         "finals" : 0
#                     },
#                     "introduction_to_computing" : {
#                         "prelims" : 0,
#                         "midterms" : 0,
#                         "prefinals" : 0,
#                         "finals" : 0
#                     }
#                 }
#             },
#             "bscomsci" :
#             {
#                 "1st_semester":
#                 {
#                     "no available subjects" : None
#                 }
#             }
#         }
#     },
#     {
#         "year_2_subjects" : {
#             "bsit" : 
#             {
#                 "1st_semester" : 
#                 {
#                     "subject" : "no available subject."
#                 }
#             }
#         }
#     },
#     {
#         "year_3_subjects" : {
#             "bsit" : 
#             {
#                 "1st_semester" : 
#                 {
#                     "subject" : "no available subject."
#                 }
#             }
#         }
#     },
#     {
#         "year_4_subjects" : {
#             "bsit" : 
#             {
#                 "1st_semester" : 
#                 {
#                     "subject" : "no available subject."
#                 }
#             }
#         }
#     },
# ]



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
            
            x = None
            x = int(input("[#] Choose a year level: "))
            year_chosen = subjects[x - 1]
        
            for year_level, courses in year_chosen.items():
                print(f"[#] Courses available in {year_level}")
                

                course_list = list(courses.keys())
                for i, course in enumerate(course_list, start=1):
                    print(f"[{i}] : {course}")
                

            
            
        elif x == 2:
            break

 
    


    except Exception as e:
        print("\n[!] Invalid input\n")