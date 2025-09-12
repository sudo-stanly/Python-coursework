
"""

    * rows and column...

"""

#! using range() function.
#* range function returns a sequence of numbers, starting from 0 by default and increments by 1 (by default), and stops
#* before a specified number.

"""
    !SYNTAX:
    * range(start, stop, step)
"""


rows = 5
#!      Parameter               Description
#*      start                   optional. an integer number specifying at which position to start. Default is 0
#*      stop                    required. an integer number specifying at which position to stop (not included)
#*      step                    optional. an integer number specifying incrementation. Default is 1            

#! example:
# for x in range(0, rows): #* start and stop
#     print(f"row {x} *")    
    
    
#create a sequence of numbers from 3 to 5, and print each item in the sequence.
# x = range(3, 6) #! start and stop
# for n in x:
#     print(n) #* prints 3 4 5
    
#create a sequence of numbers from 3 to 19, but increment by 2 instead of 1
# x = range(3, 20, 2) #! start, stop and step. the step parameter is an incrementation either 1 or 2 depende.
# for n in x:
#     print(n) #* prints 3, 5, 7, 9, 11, 13, 15, 17, 19


#! try:
"""
    ! GRID TABLE

*        col     col     col     col     col
* rows   0.0     0.1     0.2     0.3     0.4
* rows   1.0     1.1     1.2     1.3     1.4
* rows   2.0     2.1     2.2     2.3     2.4
* rows   3.0     3.1     3.2     3.3     3.4
* rows   4.0     4.1     4.2     4.3     4.4

"""
#! example:

#* 1 row
# for row in range(1):
#     print(f"row: {row}")
    
#* 1 row, 1 column
# for row in range(1):
#     for col in range(1):
#         print(f"row: {row}, column {col}")
    
    #* row is an outerloop. outer loop is how many times we want to loop.
    #* column is an inner loop, inner loop is how many times it loops each outerloop or row.
    
#* 1 row, 3 columns
# for row in range(1):
#     for col in range(3):
#         print(f"row {row}: column {col}")

#* formatting exact columns in its specified row:
# for row in range(1):
#     for col in range(3):
#         print(f"[{row} , {col}]", end=" ") #* prints as [0, 0], [0, 1], [0, 2]
#     print("<- end of row, next line [can be left empty print()]")