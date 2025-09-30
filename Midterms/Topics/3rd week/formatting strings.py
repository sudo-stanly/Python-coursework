#* formatting strings
name = "Alice"
age = 30

# f-string is where can put positional variables, the old way of doing it is .format() function
formatted_string = f"My name is {name} and I am {age} years old."


#example 2: using str.format() method
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
    # the empty brackets will place the variables that we passed in the parameters of the format function
    # depending on its position.
    
#example 3: using % operator
formatted_string3 = "My name is %s and I am %d years old." % (name, age)

#example 4: formatting numbers
pi = 3.1415926535
formatted_string4 = f"Pi rounded to 2 decimal places is {pi:.2f}"

#example 5: formatting with width and alignment:
formatted_string5 = f"|{'Name':<2}: {name:>10}|{'Age':^5}: {age:^10}"

#example 6: formatting with thousands separator
number = 1000000000
formatted_string6 = f"The number is {number:,}"

#example 7: formatting with percentage
percentage = 0.256
formatted_string7 = f"The success rate is {percentage:.2%}"
    # this adds a percentage after a decimal precision
    
#example 8: formatting with scientific notation:
large_number = 1234567890
formatted_string8 = f"The large number in scientific notation is {large_number:.2e}"
    # this is used during scientific calculations when the calculator cant fit the numbers
    
#example 9: using format specifier in str.format()
formatted_string9 = "My name is {0} and I am {1} years old".format(name, age)

#* what makes fstring different from format?
    # f string is the new version of format, because it gives control of the variable position.


print(formatted_string9)