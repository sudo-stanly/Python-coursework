
#! nested dicts
# a nested dictionary is just a dictionary inside anither dictionary

# example we have a nested dict in student, which is the value of details key.
# name is a key with a simple value "Linus".
# details key has a value that is another dictionary.
student = {
    "name": "Linus",
    "details": {
        "age": 55,
        "course": "BSIT",
        "year": 3
    }
}

#printing the keys
for keys in student.keys():
    print(keys)
    
print()
# details is a dictionary itself

#* accessing nested dictionaries
#first lets print the basic way
print(student["details"]) #output: {'age': 55, 'course': 'BSIT', 'year': 1}
# this prints the whole inner dictionary value of the key details.

print()

#* accessing specific value inside "details"
print(student["details"]["course"]) #output: BSIT
# the format is dict["outer_key"]["inner_key"]

print()

#! try:
# access the age key pair from the details key.
print(student["details"]["age"]) #output: 55

print()

#! looping through inner dictionary:
# explain: first we access the outer key 'details' then get the pairs with items function
# then the loop prints them one by one.
for key, value in student["details"].items():
    print(f"{key} : {value}")
    
print()
    
#! outer loop + inner loop:
for key, value in student.items():
    if isinstance(value, dict):
        print(f"{key}: ")
        for inner_key, inner_value in value.items():
            print(f"\t{inner_key} : {inner_value}")
    else:
        print(f"{key} : {value}")   
        
print()    
"""

# explain: so we use for loop to access the key-value pairs first wiht items function
# then we used the isinstance method to check if the value is a dictionary
# if it returns true we print key and then we declare another loop inside
# the inner key is the keys of the inner dictionary and the inner value is the value of
# the inner key, we access them through value since it's inside another dictionary
# the hirearchy of the nested dictionary is: 

    student = 
    {
      "name" : "Linus
      "details" : {
            "age": 55,
            "course": "BSIT",
            "year": 3
       } 
    }
    so if the value is an instance of a dictinoary
    we can then get the pairs inside the value element of the first outer loop
    using the items function.


    why do we loop through the value and not the key?
    "details" is they key
    the actual inner dictionary '{"age":55, "course":"BSIT", "year":3}' is the value of that key
    
    if we loop through the key, we would just loop over the string details since key="details",
    which is not what we want.
"""
# example
for key, value in student.items():
    print(f"key : {key}")
    print(f"\titems : {value}")
    print()
    
print()
"""
    # so to really access the nested dictionary we must loop over it.
    
    # visualize it as:
    
    #! student is a box
        #* "details" is just a label on the box
        #* the actual smaller box (the inner dictionary) is inside the value
        # so we really want to open the smaller box, we don't look at the label
        # we open the box itself the "value".
"""
# example
box = {
    "toolkit" : ["magnetic screwdriver", "claw hammer", "sledge hammer", "heavy duty scissors"],
    "manufacturer" : {
        "name" : "kobalt",
        "founder" : "Willard Ahdritz"
    }
}
# for example we have a box, inside the box there is a toolkit, then there's another box inside
# with the manufacturers information.
# we only want to get the data of the manufacturer

#example
for label, value in box.items():
    #we're now inside the box, there are two keys or labels 'toolkit' & 'manufacturer'
    # we only want what's inside the manufacturer label, we have to first check an
    # instance of a value if it is a dictionary for us to be able to print it.
    if isinstance(value, dict):
        print(f"[*] Data of {label}: ")
        for key, data in value.items(): # we access what's inside of the value using items function
            print(f"\t{key} : {data}")
print()

# but what if we only want to see the toolkit?
for label, value in box.items():
    if not isinstance(value, dict):
        print(f"[*] Data of {label}")
        #! print(f"\t{value}")
        
        #! important
        # so how do we print a list value that is inside of a dictionary?
        # we print them normally but coming from the value
        # for item in value:
        #     print(f"item : {item}")
            
        #! important
        # so how about indexing them? we can use enumerate.
        for index, item in enumerate(value, start=1):
            print(f"[{index}] {item}")
print()

# what if we only want a specific data from the manufacturer which we don't know what it could
# possibly be?
# this is where we use the find/search and check to see inside the manufacturer.
key = "ceo"
# if we know the key we direct access
if key in box["manufacturer"]:
    print(f"{key} : {box["manufacturer"][key]}")
else:
    print(f"{key} not found.")

# else if we're not sure we use the get() function
print(f"{key} is {box.get(key, 'not found')}")

print() 