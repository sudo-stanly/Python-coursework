
#* =============================================
#* TOPIC : Name casing and Variable assigning multiple values
#* =============================================

"""

    * Name casing:
    ! A variable name must start with a letter or the underscore character (ex: _myvar )
    ! A variable name cannot start with a number (ex: 1myvar )
    ! A variable name can on;y contain alpha-numeric characters and underscores ( A-z, 0-9, and _ )
    ! Variable names are case sentive (age, Age and AGE are three different variables)
    ! A variable name cannot be any of the Python keywords
    
"""

#! examples:

#* Camel Case
varName = None

#* Pascal Case
VarName = None

#* Snake Case
var_name = None

#* constants
PI = 3.14
MAX_USERS = 100
MIN_PASSWORD_LENGTH = 8




"""

    * Assigning multiple values to a variable: 
    ! Python allows you to assign values to multiple variables in one line.

"""

#! examples:

#* variable1, variable2 = value1, value2
x, y = 123, 321
#print(f"x: {x} y:{y}")

#* you can also assign multiple values in one variable
var = "Orange", "Banana", "Cherry"
#print(var) #which will be converted to a tuple ( lol )

#* if you have a collection of values in a list, tuple etc. Python allows you to
#* extract the values into variables. This is called `unpacking`
fruits = ["Orange", "Banana", "Apple"]
x, y, z = fruits
#print(f"x is\t:\t{x}\ny is\t:\t{y}\nz is\t:\t{z}")