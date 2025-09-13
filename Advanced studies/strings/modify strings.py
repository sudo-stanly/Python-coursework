"""

    ! modify strings

"""

#! upper case:
#* the upper() method returns the string in upper case.
a = "Hello, World!"
# print(a.upper()) #* prints "HELLO, WORLD!"


#! lower case:
#* the lower() method returns the string in lower case.
# print(a.lower()) #* prints "hello, world!"


#! remove whitespace, strip():
#* the strip() method removes any whitespace from the beginning or the end.
b = " Hello, World! "
# print(f"from ' Hello, World! ' to '{b.strip()}'")


#! replace string, replace():
#* the replace() method replaces a string with another string.
# print(b.replace("H", "J")) #* prints Jello, World!


#! split string, split():
#* the split() method splits the string into substrings if it finds isntances of the separator.
# print(b.split(",")) #* returns ['Hello', ' World!']