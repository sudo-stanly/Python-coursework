"""
    ! PYTHON DATA TYPES ASSIGNMENT:
    
    * converting variable type and reassigning a variable
"""

#* example of TYPE CONVERSION and REASSIGNMENT:

# x is first initialized with a number type, then converted to a string,
# the output will is: "8700" (without the double quotes) and dont forget
# the hashtag ;)
x = 8700
x = str(x)
print(x)

# y is first initialized with a string type but with a number, then converted
# to a number type.
y = "500"
y = int(y)
print(y)

# but converting a sentence into a number is invalid because the interpreter
# will detect it as a string literal and not a number.
    # z = "Num"
    # z = int(z)
    # print(z)

#* When do we use this type conversion or reassigning values?
# we use reassignment when we want to assign a new value to a variable.
w = 10
w += 10   #* -> compound operators can reassign new value to the variable.
w **= 3   #* -> 20 ** 3 = 20 x 20 x 20 = 8000
print(w)


#we use type conversion when we want to change the type of a specific value of a variable.
z = 90000
z = str(z)
print(z)

#we can also reconvert a string number back to a number type
z = int(z)
print(z)