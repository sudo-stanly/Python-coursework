
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

#! findall:
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

#! search() function:
#* the search function searches the string for a match, and returns a 'Match Object' if there is a match.
#* if there is more than one match, only the first occurence of the match will be returned:

    #! first the match object:
    #* a match object is an object containing information about the search and the result.
    #* Note: if there is no match, the value None will be returned, instead of the Match Object.
    
#* example:

#do a search taht will return a Match Object:
x=re.search("ai", txt)
#print(x) #this will print an object

#* the match object has properties and methods used to retrieve information about the search, and the result:
"""

    ! .span():
    * returns a tuple containing the start-, and end positions of the match.
    
    ! .string
    * returns the string passed into the function
    
    ! .group()
    * returns the part of the string where there was a match

"""

#! span() example:
#* print the position (start- and end-position) of the first match occurence.
#* the regular expression looks for any words that starts with an upper case "S"

#* search for an upper case "S" character in the beginning of a word, and print its position.
x = re.search(r"\bS\w+", txt)
#print(x.span()) #* prints (12, 17) (start, end) 

    #! try
    #* \b start position?, \w end position?
y = "I like pizza"
# y = re.search(r"\ba\w+", y) #! wrong
# print(y.span())

    #* \b means word boundary or start of a word, ^ means beginning of a string, $ end of string, end of word is Z\b, while beginning is \bZ 
    #* \w+ means end of one or more word characters
# y = re.search(r"\bp\w+", y)
# print(y) #! wrong: only use \b ... \w+ to find a start of a word. 

#! a\b means word that ends with "a", \ba means word that starts with "a"
# y = re.search(r"a\b", y)
# print(y.span())

#* searching in between
"""
    ! + means one or more: atleast one cahracter after the first 'a'
    ! * means zero or moreL allows a as a full word
"""

z = txt="Lorem ipsum dolor sit amet consectetur, adipisicing elit." 
# find = re.findall(r"\b\w*i\w*\b", z) #* words containing i
# print(find)


#! try:
#* words that starts with 'a'
# findChar = re.findall(r"\ba\w*", z)
# print("words that starts with 'a': ", findChar)


#* words that ends with 'm'
# findChar = re.findall(r"\b\w*m\b", z) #* using r"a\b" only returns a one word of m
# print("words that ends with 'm': ", findChar)


#* use * if you want to  allow zero characters allowing even a single character like 'a' inside of a list ['a', 'apple', 'area']
#* use + if you want to only allow atleast one more which excludes a character 'a' from the list ['apple', 'area']
# w = "a apple area"
# w = re.findall(r"\ba\w+", w)
# print(w) #* prints ['apple', 'area']

# w = re.findall(r"\ba\w*", w)
# print(w) #* prints ['a', 'apple', 'area']


#! going back to match object functions:
#! summary: use span() to find the start and end of a string that you want to search
txt = "minumulto na ako ng damdamin ko."
find = re.search(r"\b\w*o\b", txt) #* search function only returns the first match
# print(find.span())




#! string example:
#* returns the string passed into the function

#first we try to search for an upper case "S" cahracter in the beginning pf a word and return its position using span
word = "The rain in Spain"
# word = re.search(r"\bS\w+", word)
# print("Position of 'S' is: ", word.span()) # returns (12, 17)

#* now print the string passed into the function
#* the string property returns the search string:
# print(word.string) #returns the whole string when match is found

#* to return the exact match we use the group() property 
# print(word.group())

#! if there is no match, the value None will be returned, instead of the Match Object.


"""

    ! split() function
    * the split() function returns a list where the string has been split each match.

"""

#! example: split at each white space character
# word = re.split("\s", word)
# print(word) #* returns a list ['The', 'rain', 'in', 'Spain']

#* you can also control the number of occurences by specifying the maxsplit parameter.
#! re.split('\s', variable, maxpslit_parameter)
word = re.split("\s", word, 1)
print(word) #* returns a list ['The', 'rain in Spain']