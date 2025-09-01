
#* Advance study about syntax, data types, variables, and scope


#! SYNTAX
"""
    ! PYTHON INDENTATION:
        Indentation refers to the spaces at the beginning of a code line.
        Where in other programming languages the indentation in code is for 
        readability only, the indentation in Python is very important.
        Python uses indentation to indicate a block of code.
"""

# *example 1:
if 5 > 2:
    print(True); # -> no errors
    
#if 5 > 2:
#print(True) # -> indentation error

# *example 2:
#if 5 > 2:
#    print(True)
#        print(True) # -> indentation error
        
if 5 > 2:
    print(True)
    print(True) # -> the number of spaces or tab must be aligned with the first indentation.
    
    

#! PYTHON VARIABLES:

# *example 1:
num , str = 5, "Hello, World!"; print("num:",num," str:",str);



#! COMMENTS

#* Single line comment
""" 
    *multi line comment with triple quotes
"""


#! DATA TYPES

# string, int, float, bool, list, tuple, dictionary, set, frozenset, nonetype

str = "string" #to form a sentence or something
charStr = 'string' #still the same as "string"

#num can be in positive or negative
num = 123
num = -123

#example arithmetic operation
num = 143 - 132
#print(num)


#floating num : this data type takes a number with a decimal while int does not
fl = 12.00000008899

#boolean value returns true or false, but in reality there are falsely and truthfully expressions
#but during operations a boolean of true may return 1, false to 0, and others.
bn = False

#example
op = True + True < (5 + True)
# print(op)

#list
ls = ["apple", "orange", "banana"]

#* CHANGEABLE (mutable)
#lists are mutable which means elements inside the list can be changed.
ls[0]="hello world"
# print(ls)

#* ORDER
    # When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
    # If you add new items to a list, the new items will be placed at the end of the list.

#* LIST METHODS
    
#! 1. append(): adds an element at the end of the list
ls.append("new item")
#print(ls)

#! 2. clear(): removes all the elements from the list
ls.clear()
print("cleared:", ls)
ls.append("¯\_(ツ)_/¯")
#print("cleared:", ls)

#! 3. copy(): returns a copy of the list
anotherList = [1, 2, 3]
copyOfList = anotherList.copy()
ls.append(copyOfList)
#print("the copied list: ", ls[1])

#! 4. count(): returns the number of elements with the specified value
ls.append("cherry")
x = ls.count("cherry")
print(x)

#!5. extend(): Add the elements of a list (or any iterable), to the end of the current list
ls_1 = ["hello world"]
ls_2 = [1, 2, 3, "cherry"]
ls_1.extend(ls_2)
#print(ls_1)

#! index(): returns the index of the first element with the specified value
x = ls_2.index("cherry")
#print("the index of \"cherry\" is:",x)

#! insert(): adds an element at the specified position
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
#print(fruits) #banana will become index 2, while orange takes the position of 1

#! pop(): removes the element at the specified position
fruits.pop(1) #removed 'orange' from the list
#print(fruits)

#! remove(): removes the item with the specified value
fruits.remove("banana")
#print(fruits) #removed banana from the list

#! reverse(): reverses the order of the list
countries = ["Philippines", "Japan", "Korea"]
countries.reverse()
#print(countries) #reverses the order of the list

#! sort(): sorts the list
cars = ["Ford", "BMW", "Volvo"]
cars.sort()
#print(cars)

alphabet = ["A", "Z", "C"]
alphabet.sort()
#print(alphabet)

    #you can also make a function to decide the sorting criteria
    #*SYNTAX: list.sort(reverse=True|False, key=myFunc) 
    #PARAMETER              DESCRIPTION
    #reverse 	Optional. reverse=True will sort the list descending. Default is reverse=False
    #key 	Optional. A function to specify the sorting criteria(s)
    
#example:
alphabet.sort(reverse=True)
#print(alphabet) #sorts in reverse

cars.sort(key=len) #this checks the length of each key then sorts by its lowest to highest length, ex: FORD: 4, BMW: 3, VOLVO: 5
#it will then print in order from lowest to highest length, 3, 4, 5 ['bmw', 'ford', 'volvo']
#print(cars)

#*in this example of dictionary, sort a list of dictionaries based on the "year" value of the dictionaries.

# list and dictionary is similar to array and objects in javascript.

cars_2 = [
    {
        'car' : 'Ford', 'year' : 2005
    },
    {
        'car' : 'Mitsubishi', 'year' : 2000
    },
    {
        'car' : 'BMW', 'year' : 2019
    },
    {
        'car' : 'VW', 'year' : 2011
    }
]
cars_2.sort(key=lambda e: e['year']) #lambda is a short function, takes a parameter of e, then returns e with keys of year and gets sorted from lowest to highest
#print(cars_2)

#*Sort the list by the length of the values and reversed:
cars_3 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars_3.sort(reverse=True, key=lambda e: len(e))
print(cars_3)




#! SCOPE
"""
    !LOCAL & GLOBAL VARIABLE SCOPE
"""
globalVar = "I am global"

def myFunc():
    localVar = "I am local"
    #print(globalVar)
    
myFunc()
#print(localVar) # -> localVar is not defined within this scope


"""
    ! If you create a variable with the same name inside a function, this variable will be local, 
    ! and can only be used inside the function. The global variable with the same name will remain as it was, 
    ! global and with the original value.
"""
x = "Hello, World!"
def myFuncFunc():
    x = "I am now local"
    #print(x)
myFuncFunc()
#print("I am global again: ", x)



"""
    ! Global keyword: Normally, when you create a variable inside a function, 
    ! that variable is local, and can only be used inside that function.
"""
def globalFunc():
    global y
    y = "awsome"
globalFunc()
#print("Python is ", y)


#* Also, use the global keyword if you want to change a global variable inside a function.
z = "awsome"
def globalFuncFunc():
    global z
    z = "fantastic"
globalFuncFunc()
print("Python is ", z)



