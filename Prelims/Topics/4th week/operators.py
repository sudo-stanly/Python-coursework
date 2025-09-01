
#* =============================================
#* TOPIC : Operators
#* =============================================

"""
    ! Python divides operators in the following groups:
    * Arithmetic operators
    * Assignment operators
    * Comparison operators
    * Logical operators
    * Identity operators
    * Membership operators
    * Bitwise operators
    
"""

#! examples:

#* Arithmetic operators : Arithmetic operators are used with numeric values to perform common mathematical operations.
#x,y = True + True #* addition
#x,y = True - True #* subtraction
#x,y = True * True #* multiplication
#x,y = True / True #* division (quotient)
#x,y = True % True #* modulus (remainder)
#x,y = True ** True #* exponentation (how many times you divide it by itself)
#x,y = True // True #* floor division (returns with no decimal output || rounds the result down to the nearest whole number)


#* Assignment operators : Assignment operators are used to assign values to variables:
#!  Operator    Example      Same As
#*    =          x = 5        x = 5   : the = operator is used to assign a new value to a variable.
z = 5
#print(z)

#*   +=          x += 3       x = x + 3 : += adds a new value to the variable by addition, since x is 5 then x += 3 is similar as x = x + 3 then it is equals to 8
z += 3
#print(z)

#*   -=          x -= 3       x = x - 3 : this subtracts the recent value which is 8, then returns to the original value of 5
z -= 3
#print(z)

#*   *=          x *= 3       x = x * 3 : this multiplies to 3, 5 x 3 = 15
z *= 3
#print(z)

#*   /=          x /= 3       x = x / 3 : this divides to 3, 5 / 3 = 5 (this is the quotient)
#z /= 3
#print(z)

#*   %=          x %= 3       x = x % 3 : this divides and gets the remainder of 5 / 3
#z %= 3
#print(z)

#*   //=          x //= 3       x = x / 3 : floor division rounds the result down to the nearest whole number
#z //= 3
#print(z)

#*   **=          x **= 3       x = x ** 3 : exponentation operator multiplies by itself by how many times you want it to. 15! = 3...
z **= 3
#print(z)




#*  Comparison Operators: comparison operators are used to compare two values:
#!  Operator            Name                            Example
#*    ==                Equal                           x == y : this checks if the value is same as what is being referenced to, like a variable or exact value.
w = 5
m = 3
#print(w == m)

#*    !=                Not equal                       x != y : this checks that first operand is not the same value as the 2nd operand
w = 5
m = 3
#print(w != m)

#*    >                 Greater than                     x > y : this checks if the first operand is higher than the 2nd operands value
w = 5
m = 3
#print(w > m)

#*    <                 Lesser than                      x < y : this checks if the first operand is lessser than the 2nd operands value
w = 5
m = 3
#print(w < m)

#*    >=                Greater than or equal to        x >= y : this checks if the first operand is greater than or equal to the 2nd operands value
w = 5
m = 3
#print(w >= m) # returns True because five is greater, or equal, to 3

#*    <=                Lessert than or equal to        x >= y : this checks if the first operand is lesser than or equal to the 2nd operands value
w = 5
m = 3
#print(w <= m) # returns false because 5 is neiter less than or equal to 3


#*  Logical Operators: logical operators are used to combine conditional statements and words instead of symbol..
#!  Operator            Description                                                         Example
#*  and                 Returns True if both statements are true 	                    x < 5 and  x < 10
#print(w < 5 and w < 10)

#*  or                  Returns True if one of the statements is true 	                x < 5 or x < 4
#print(w < 5 or w < 10)

#*  not                 Reverse the result, returns False if the result is true 	  not(x < 5 and x < 10) 
#print(not(w < 5 and w < 10))	



#*  Identity operators: identity operators are used to compare the object, not if they are equal, but if they are actually the same object,
#*                      with the same memory location       
#!  Operator            Description                                                         Example
#*     is               Returns True if both variables are the same object                  x is y
#print( w is m )

#*     is not           Returns True if both variables are not the same object 	            x is not y
#print( w is m )


#*  Membership Operators: Membership operators are used to test if a sequence is presented in an object:
#!  Operator            Description                                                         Example
#*    in  	            Returns True if a sequence with the specified value                x in y
#*                      is present in the object
ls = ["Apple", "Banana", "Orange"]
#print( "Banana" in ls )

#*  not in 	            Returns True if a sequence with the specified value               x not in y
#*                      is not present in the object 
#print( "Banana" not in ls )