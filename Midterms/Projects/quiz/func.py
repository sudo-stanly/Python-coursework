
sample_grades = [85, 90, 78, 92, 88]
print(f"Student grades: {sample_grades}")

def calculate_average(grades):
    SUM = sum(grades) / len(sample_grades)
    print(f"AVERAGE: {SUM}")    

    get_status(SUM)

def get_status(average):
    if average >= 75:
        print("STATUS: PASS") 
    else:
        print("STATUS: FAIL") 

calculate_average(sample_grades)