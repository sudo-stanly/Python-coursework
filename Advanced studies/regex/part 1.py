
"""

    * a RegEx, or Regular Expression is a sequence of characters that forms a search pattern.
    * RegEx can be used to check if a string contains the specified search pattern.
    
    * Python has a built-in package called re, which can be used tow work with Regular Expressions.
    
    #! import the re module

"""

import re

"""

    * When you have imported the re module, you can start using reular expressions

"""

#! examples:

#* Search the string to see if it starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The. *Spain$", txt)

if x:
    print("YES! we have a match!")
else:
    print("No match")
    
    
    #! so im guessing ^ means start with and *$ means ends with?
    

"""

    * RegEx functions
    * The re module offers a set of functions that allows us to search a string for a match.
    
    ! findall
    * returns a list containing all matches
    
    ! search
    * returns a match object if there is a match anywhere in the string
    
    ! split
    * returns a list where the string has been split each match
    
    ! sub
    * replaces one or many matches with a string

"""

#! examples:

#* findall:
txt = "The rain in Spain"
x=re.findall("ai", txt) #! hmm... re.findall( "value_to_find", variable_containing_that_value )
#print(x) #* This will return a list containing every occurence of "ai"

    #* the list contains the matches in the order they are found.
    # * if no matches are found, an empty list is returned:
x=re.findall("Portugal", txt)
#print(x)
# if x:
#     print("Yes, there is at least one match")
# else:
#     print("No match")