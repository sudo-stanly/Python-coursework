# basic dictionary
student = {
    "name": "Linus",
    "age": 19,
    "course": "BSIT"
}
#accessing values
print(student["name"])

#adding new key/value
student["year"] = 1
print(student)


#! removing from dictionary
#* removing a dictionary key pair using 'del' keyword, del must be declared first and after a dictionary to delete with key pair:
del student["name"]
print(student) #output: {'age': 19, 'course': 'BSIT', 'year': 1}


#* removing using the pop method, the pop method only accepts an integer input:
my_dict = {1:"Linus", 2:"Van", 3:"Steve"}
# data = my_dict.pop(1)
# print(data) # prints the removed pair
# print(my_dict) # output: {2: 'Van', 3: 'Steve'}


#* how to remove using the pop item, the pop method does not accept any input which means
#* the element that needs to be removed cannot be specified:
deleted_key = my_dict.popitem()
print(deleted_key) # prints the removed item which is 3
print(my_dict) # output: {1: 'Linus', 2: 'Van'}


#* how to remove multiple keys from a Dictionary,
#* by doing that we can easily delete multiple keys using the .pop() method in Python,
#* used in a loop over a list of keys, is the safest approach for doing this

#declare dict
my_dict = {"name" : "Linus", "age" : 35}

# define the keys to remove
keys = ['name', 'age']

# remove keys
for key in keys:
    my_dict.pop(key, None)
print(my_dict) # output: {}
# inside the pop method we pass in 'None' and the default value, just to make sure
# no KeyError is printed if a key doesn't exist.


#* how to remove all keys from dict using the clear method
#* you can use the clear() method to remove all key-value pairs from a dictionary:
dict = { "name" : "Linus" }
dict.clear()
print(dict) # output: {}


#* conclusion:
# for removing a key-value pair or several key-value pairs from a dictionary,

#! 'del' keyword
# using 'del' keyword is the most common method of removing a key-value pair
# from a dictionary.


#! pop() method
# the pop() method is useful when we need to remove a key-value pair and also 
# get the value of the key-value pair.

#! popitem() function
# we can remove the final key-value pair in a dictionary