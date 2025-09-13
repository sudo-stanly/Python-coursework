"""

    ! Python logical operators
    * in python the logical operators are literal and not symbols
    * && -> and
    * || -> or
    * ! not

"""

x = 5

# print( x < 5 and x < 10 ) #* the and operator only executes if both operands are true, if the first operand
                            #* falls to false it will return false.
                           
# print( not(x < 5 and x < 10) ) #* the not operator will reverse the boolean value of the operands
                               #* false -> true, true to false.
                               #* since first operand is now true, it will return true. 

#* imagine it like this:
# print( True and True )  #* True since the first operand is true.
# print( False and True ) #* False since the first operand is false.
# print( True and False ) #* False since the second operand is true.

#! or operator
#* this only returns for true value if one becomes false
# print("is x lower or higher than 5? ",x < 5 or x < 10) #* first operand is false, 2nd operand is true

#* imagine it like this
# print( False or True ) #* it will always return true since the second operand is true.



#! when to use these operators?
#* by using and operator, it is used when both operands are true, for example if age >= 18 and isStudent, both are to be true
#* if one becomes false this will not execute.
isStudent = True
age = 20
if age >= 18 and isStudent:
    print("hello")


#* by using the or operator, it will only execute if one of the operands is true.
if age >= 18 or age < 18:
    print("welcome")
    
#* by using the not operator, it will reverse the boolean values of the operands, true to false, false to true
x = True
if not x:
    print(f"value of x is {x} now it is {not x}") #* this will not execute because the value of x became false.
    
    #* example we have a set and want to check if a character is within that set
allowedChars = ('$^&*()')
userInput = "lorem ipsum $"
if not all(char in allowedChars for char in userInput):
    print("hello world")