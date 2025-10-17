
#! avoid using predefined functions (sum, len)
#! typos
#! function call
# sample_grades = [85, 90, 78, 92, 88]
# print(f"Student grades: {sample_grades}")

# def calculate_average(grades):
#     SUM = sum(grades) / len(sample_grades)
#     print(f"AVERAGE: {SUM}")    

#     get_status(SUM)

# def get_status(average):
#     if average >= 75:
#         print("STATUS: PASS") 
#     else:
#         print("STATUS: FAIL") 

# calculate_average(sample_grades)


#* correction
# i will write my own way without predefined functions
# function calls are corrected by instructor

sample_grades = [85, 90, 78, 92, 88]
print(f"Student grades: {sample_grades}")

def calculate_average(grade):
    
    length = 0
    for i in grade:
        length += 1
        
    sum = 0
    for i in grade:
        sum += i
        
    return sum / length

def get_status(average):
    if average >= 75:
        print(f"AVERAGE\t: {average}\nSTATUS\t: PASS")  
    else:
        print(f"AVERAGE\t: {average}\nSTATUS\t: FAIL")

get_status(calculate_average(sample_grades))