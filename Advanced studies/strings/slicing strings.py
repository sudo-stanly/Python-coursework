"""

    ! slicing strings
    * you can return a range of characters by using the slice syntax.
    * specify the start index and the end index, separated by a colon, to return a part of the string.

"""

#! x[start : end]
b = "hello, World!"
#*   012345678910
# print(b[2:5]) #* prints "llo"
#* the first character has index 0.


#! slice from the start: [:end]
#* by leaving out the start index, the range will start at the first character.
# print(b[:5]) #* prints "llo"


#! slice to the end: [start:]
#* by leaving out the end index, the range will go to the end.
# print(b[2:]) #* prints "llo, World!"

#! negative indexing: [-start : -end]
#* use negative indexes to start the slice from the end of the string.
# get the characters:
# from: "o" in "World!" (position -5)
# to, but not included: "d" in "World!" (position -2):
#! b = "H   e   l   l   o   ,       W   o    r    l  d   !"
#*      0   1   2   3   4   5   6   7   8    9   10  11  12
#*    -13 -12  -11 -10 -9  -8  -7  -6  -5   -4   -3  -2  -1
# print(b[-5:-2]) #* prints "orl" because -5 is i, -4 is r, -3 is l and -2 is d which stops before reaching that index.