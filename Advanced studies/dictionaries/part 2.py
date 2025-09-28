
#! Accessing Dictionaries with For Loops

# declare
student = {
    "name" : "Linus",
    "age" : 55,
    "course" : "BSIT"
}

#! Part 1
#* printing all dictionary keys
# this prints all the keys in student: name, age, course.
for key in student:
    print(key) 
    
print()

#! Part 2
#* printing all dictionary values
# this prints all the values of the keys in dictionary.
for key in student:
    print(student[key])
    
print()
    
#! testing:
# print all keys and values of a dict using the key element in for loop
for key in student:
    print(f"[{key}]\t: {student[key]}")
    
print()

#! Part 3
#* printing both key and value with items() function this way we don't have 
#* to use one key to access the values inside of the dictionary.
# this way we dont haev to use "print(dict[key])" instead we use key, value
# we use items() to access the pairs.
for key, value in student.items():
    print(f"[*] {key} : {value}")
    
print()
    
#! methods of getting the pairs:
#* .keys() : this method gives us the key pairs in the dictionary:
print("keys:")
for keys in student.keys():
    print(f"[*] {keys}")
    
print()
    
#* .values() : this method gives us the value pairs of a key in the dictionary.
print("Values:")
for values in student.values():
    print(f"[*] {values}")
    
print()

#* .items() : this method gives us both of the pairs in dictionary which is 
#* key and value.
print("Items:")
for key, value in student.items():
    print(f"[*] {key} : {value}")

print()

#* to add numbering when printing a dictionary, we use the enumarate method
#* but in this case we have to declare index and key element in for loop and
#* print the values using the key pair
# the enumerate function accepts one or 2 parameters, iterable and start
# for iterable, we put an iterable object which is a list or a dictionary
# by default it starts with 0, to change that we use the start parameter
# this is a number defining the start number of the enumerate object.
# example: enumerate(myDict, start=1), indexing starts with 1 by default
print("Enumerate:")
for index, key in enumerate(student):
    print(f"[{index}] {key} : {student[key]}")
    
print("Enumerate:")
for index, key in enumerate(student, start=1):
    print(f"[{index}] {key} : {student[key]}")