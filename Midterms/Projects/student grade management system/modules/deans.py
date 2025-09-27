import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

SCHOOL = [
    {
        "IT_DEPARTMENT" : {
            "BSIT" : [
                {
                    "1st_year" : {
                        "1st_semester" : ["programming_1", "introduction_to_computing", "visual_arts_and_crafts", "nstp_1_cwts"],
                        "2nd_semester" : ["programming_2", "principles_of_accounting", "web_system_and_technologies"]
                    },
                },
                {
                    "2nd_year" : {
                        "1st_semester" : ["gender_and_society", "understanding_the_self", "event_driven_programming", "integrative_programming_1", "object_oriented_programming", "human_computer_interaction"],
                        "2nd_semester" : ["data_structures_and_algorithm", "platform_technologies", "discrete_mathematics", "living_in_the_it_era", "purposive_communication", "integrative_programming_2", "advanced_database_management_system"]
                    },
                },
                {
                    "3rd_year" : {
                        "1st_semester" : ["app_development", "python_programming", "system_analysis_and_design", "mathematics_in_the_modern_world", "networking_1", "information_assurance", "quantitatve_methods"],
                        "2nd_semester" : []
                    },
                },
                {
                    "4th_year" : {
                        "1st_semester" : [],
                        "2nd_semester" : []  
                    }
                }
            ]
        }
    },
    {
        "MARKETING_DEPARTMENT" : []
    }
]                   

print("Available departments: ")
for row, school in enumerate(SCHOOL, start=1):
    for department in school.keys():
        if str(department) != "IT_DEPARTMENT":
            format_text = str(department).replace('_', ' ').lower().title()
            print(f"[{row}] {format_text}")
        else:
            format_text = str(department).replace('IT_DEPARTMENT', 'IT Department')
            print(f"[{row}] {format_text}")     
print()
    
x = int(input("Choose department: "))