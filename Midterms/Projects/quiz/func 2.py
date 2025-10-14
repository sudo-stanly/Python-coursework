
sample_grades = [85, 90, 78, 92, 88]
print(f"Student grades: {sample_grades}")

def calculate_average(grades):
    return get_status(sum(grades) / len(grades))

def get_status(average):
    if average >= 75:
        return f"AVERAGE: {average}\nSTATUS: PASS"
    else:
        return f"AVERAGE: {average}\nSTATUS: FAIL"

print(calculate_average(sample_grades))