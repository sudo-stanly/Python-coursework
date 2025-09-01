
#* =============================================
#* TOPIC : String formatting
#* =============================================

#! examples:

#! f-string
#* f-string allows you to format selected parts of a string.
#* to specify a string as an f-string. simply put an f in front of the string literal:

txt = f"The price is 49 dollars"
#print(txt)


#! Placeholders and Modifiers
#* to format values in an f-string, add placeholders {}, a placeholder can contain
#* variables, operations, functions, and modifiers to format the value.

#! Placeholder
price = 59
txt = f"the price is {price} dollars"
#print(txt)

#! Placeholder and Modifier
#* a placeholder can also include a modifer to format the value.
#* a modifier is included by adding a colon : followed by a legal
#* formatting type, like .2f which means fixed pointer with 2 decimals

price = 59
txt = f"the price is {price:.2f} dollars" # this will add two zero decimal points
#print(txt)

#* you can also format a value directly without keeping it in a variable.
txt = f"The price is {94:.2f} dollars"
#print(txt)