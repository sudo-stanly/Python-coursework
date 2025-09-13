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
