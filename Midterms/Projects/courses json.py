
#! unpacking dictionaries

#! normal dictionary
# subject = {
#     "mathematics_in_the_modern_world" : 0
# }
# for key, value in subject.items():
#     print(f"{key} : {value}")


#! dictionary inside a list
# student = [  
#             {  
#                 "name" : "Linus Torvalds"  
#             }  
#         ]
# for key, value in student[0].items():
#     print(f"{key} : {value}")


#! dictionary inside a dictionary
# student = {
#     "name" : "Linus",
#     "subjects" : {"math": 95, "networking": 88}
# }
# for key, value in student["subjects"].items():
#     print(f"{key} : {value}")
    
    
# student_2={
#     "year_1":{
#         "course_1" : "math",
#         "course_2" : "science"
#     }
# }
# for year, courses in student_2.items():
#     print(year)
#     for course, subject in courses.items():
#         print(f"{course} : {subject}")
    
    
#! mixed
# school=[
#     {
#         "STUDENT_1":{
#             "INFORMATION":{
#                 "name" : "Linus Torvalds",
#                 "grade" : 98,
#                 "isPassed" : True
#             }   
#         }
#     },
#     {
#         "STUDENT_2":{
#             "INFORMATION":{
#                 "name" : "Van Rossum",
#                 "grade" : 98,
#                 "isPassed" : True
#             }   
#         }
#     }
# ]
# #* since this is a json form, user must index first (ig?).
# x = 2
# school_index = school[x - 1]
# for STUDENTS, info in school_index.items():
#     print(f"{STUDENTS}")
    
#     #*hierarchy, since the value of STUDENT_1 is another dictionary, access the items
#     #*of student 1 with info value.
#     for INFORMATION, data in info.items():
#         #*information is the key for "INFORMATION" inside of STUDENT_1 key
#         #*now we have access to values inside this key, now to access the information inside
#         #*we have to access the values in data
#         print(f"{INFORMATION}")
#         #* i capitalized the keys for me not to forget
    
#         for DATA, inf in data.items():
#             print(f"{DATA} : {inf}")


#! mixed
school = [
    {
        "1ST_YEAR" : {
            "IT_DEPARTMENT" : {
                    "BSIT":{
                    "1st_semester" : ["programming_1", "introduction_to_computing", "visual_arts_and_crafts", "nstp_1_cwts"],
                    "2nd_semester" : ["programming_2", "principles_of_accounting", "web_system_and_technologies"]
                },
                "COMSCI":
                {
                    "1st_semester" : [],
                    "2nd_semester" : []
                }
            }
        }
    },
    {
        "2ND_YEAR" : {
            "IT_DEPARTMENT" : {
                    "BSIT":{
                    "1st_semester" : ["gender_and_society", "understanding_the_self", "event_driven_programming", "integrative_programming_1", "object_oriented_programming", "human_computer_interaction"],
                    "2nd_semester" : ["data_structures_and_algorithm", "platform_technologies", "discrete_mathematics", "living_in_the_it_era", "purposive_communication", "integrative_programming_2", "advanced_database_management_system"]
                },
                "COMSCI":
                {
                    "1st_semester" : [],
                    "2nd_semester" : []
                }
            }
        }
    },
    {
        "3RD_YEAR" : {
            "IT_DEPARTMENT" : {
                "BSIT":{
                    "1st_semester" : ["app_development", "python_programming", "system_analysis_and_design", "mathematics_in_the_modern_world", "networking_1", "information_assurance", "quantitatve_methods"],
                    "2nd_semester" : []
                },
                "COMSCI":
                {
                    "1st_semester" : [],
                    "2nd_semester" : []
                }
            }
        }
    },
    {
        "4TH_YEAR" : {
            "IT_DEPARTMENT" : {
                    "BSIT":{
                    "1st_semester" : [],
                    "2nd_semester" : []   
                },
                "COMSCI":
                {
                    "1st_semester" : [],
                    "2nd_semester" : []
                }
            }
        }
    }
]
x = 3
chosen_year_level = school[x-1]

list_of_subjects = []

for YEAR_KEY, department in chosen_year_level.items():
    print(f"[{x}] : {YEAR_KEY}")
    
    # display departments
    for DEPARTMENT_KEY, dept_name in enumerate(department.keys(), start=1):
        print(f"[{DEPARTMENT_KEY}] : {dept_name}")
    
    # choose department
    y = 1
    school_departments = list(department.keys())
    chosen_department_name = school_departments[y - 1]
    print(f"Chosen Department: {chosen_department_name}")
    chosen_department = department[chosen_department_name]

    # display courses
    for COURSE_KEY, course_name in enumerate(chosen_department.keys(), start=1):
        print(f"[{COURSE_KEY}] : {course_name}")
        
    # choose course
    z = 1
    course_list = list(chosen_department.keys())
    chosen_course_name = course_list[z - 1]
    print(f"Chosen Course: {chosen_course_name}")
    chosen_course = chosen_department[chosen_course_name]

    # choose semester
    w = 1
    semester_list = list(chosen_course.keys())
    chosen_semester_num = semester_list[w - 1]
    print(f"Chosen Semester: {chosen_semester_num}")
    chosen_semester = chosen_course[chosen_semester_num]

    # display subjects
    for SUBJECT_KEY, subject in enumerate(chosen_semester, start=1):
        print(f"[{SUBJECT_KEY}] : {subject}")

#add subjects (instructor role)
while True:
    s = int(input("Add subjects for students: "))

