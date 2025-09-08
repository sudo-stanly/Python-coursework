
#! for loops..

#* it is used ti iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# simple demonstration
x = [1, 2, 3, 4]
#!   0  1  2  3  : indexing
#! if this was length the count will be normal 4 length, index always start with 0

i = 0 #* our index
# print(x[i]) #* accessing an list element with bracket notation and accessing by index, this prints 1

i = 1
# print(x[i]) #* prints 2 because indexed element is 1 which has an element value of 2.


#! that's where for loop comes in.
# for i in x:
#     print(i, end=" ") #* prints the whole elements inside the list
    
#! looping through string
# for char in "banana":
#     print(char, end="") #* prints each character from the string

#! break statement: this stops the loop before it has looped through all the items.
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x, end=" ")
#     if x == "banana":
#         break
    
#Exit the loop when x is "banana", but this time the break comes before the print:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x, end=" ")