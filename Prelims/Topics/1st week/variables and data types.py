
#* =============================================
#* TOPIC : Variable and Data Types
#* =============================================

# How to create variable
# Variable names
# Output variable
# Built-in Data Types

#! Variables: variables are containers for storing data values.
#* Python has no command for declaring a variable.
#* A variable is created the moment you first assign a value to it.
"""

    * variable_name     / no command for declaring
    *                   / do not need to be declared with any particular type
    
"""

# This is a string
var = "String" 

# This is still a string
var = '- in Python - \"\" or \'\' is still the same.' 

# This is an integer
x, y, z = 123, -123, 1234567 

# This is a floating number
x, y, z = 12.8888, -12.888888, 12.55 

# This is a boolean
isLogged = False 



"""

    * Reassigning variable values
    ! reassigning values is changing what's inside of an existing variable.

"""

# This will change the Hello world to 123 and also the type included.
example = "Hello world"
example = 123
#print(example)



"""

    * TYPES OF DATATYPES

    ! Text type:
    * str
    
    ! Numeric types:
    * int, float, complex
    
    ! Sequence types:
    * list, tuple, range
    
    ! Mapping type:
    * dict
    
    ! Set types:
    * set, frozenset
    
    ! Boolean type:
    * bool
    
    ! Binary types:
    * bytes, bytearray, memoryview
    
    ! None type:
    * NoneType or None
    
"""

#! examples:

#* string types:
greetings = "I am a String"
greetings = 'I am also a string'

#* numeric types:
num = 123
numFLoat = 10.0
numComplex = 100j

#* sequence types:
myList = ["apple", "orange", "banana"]
myTuple = (1, 2, 3)
myRange = range(0, 20)

#* mapping type
myDict = { "name" : "John doe", "age" : 23 }

#* set types:
mySet = {1, 2, 3}
myFrozenSet = frozenset(mySet)
#print(myFrozenSet)

#* boolean type:
isLogged = True
sum = 15 * 10 > (25 ** 30)
#print(sum)