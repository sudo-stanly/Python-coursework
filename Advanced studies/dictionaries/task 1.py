
#! Exercise: Student Record Manager
student = {
    "name": "Linus",
    "age": 55,
    "course": "BSIT"
}

#* Instructions:
# 1. Add a new key called "year" with value 1.
# 2. Update the "age" to 56.
# 3. Delete the "course" key.
# 4. Check if "course" still exists in the dictionary — if not, print "course not found".
# 5. Use .get() to safely access "course", and print "N/A" if it doesn’t exist.

#* answer:
student["year"] = 1
student["age"] = 56
del student["course"]
if 'course' in student:
    print('key found')
else:
    print('no key found')
print(student.get('course', "N/A"))

#* output:
# no key found
# N/A
