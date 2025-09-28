
#! Adding key in dictionaries:
#* adding a new key-value pair. By adding a new key-value pair
#* we can call a key as if it exists but it will add it to the dictionary.
student = {"name": "linus"}
student["age"] = 55 # output: {'name': 'linus', 'age': 55}
print(student)


#! Updating key-values in dictionary:
#* changing existing value.
student["age"] = 50
print(student) #output: {'name': 'linus', 'age': 50}


#! Checking and Searching if key exists:
#* check if key exists in dictionary.
if "name" in student:
    print(f"The key \"name\" is in students")
else:
    print("no key exists")
#output: The key "name" is in students


#* safe access with .get()
print(student.get("course"))         # this will output none or not found
print(student.get("course", "N/A"))  # this will output n/a by default if nothing is found


#* checking all keys at once
print(student.keys())