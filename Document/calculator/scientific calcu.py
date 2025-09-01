
#* no need to ask ng operation 
#* while loop
#* no match case
#* scientfic calcu
#* order of operations
#* pmdas
#* diretso na mag print dipende sa operation na nilagay sa input???

#* example: user input: "1+(3-2)"
#* then print kasama nung result

#try lang muna
#* attempt 1:
#x = input("Enter your operation: ")
#print(y)

#* attempt 2:
#x = str(int(input("Enter your operation: ")))
#print(y)

#* attempt 3:
#x = input("Enter your operation: ")
#print(y)
#while True:

#* attempt 4: provided with allowed chars
# while True:
#     x = input("Enter your operation: ")
#     y = eval(x)
#     #print(y)
#     allowed_chars = set('0123456789+-*/().^')
#     if not all(char in allowed_chars for char in expression):
#         return "Error: Invalid characters in expression"

#* attempt 5: created a function and added replace method
def func(expression):
    allowed_chars = set('0123456789+-*/().^')
    expression = expression.replace('^','**')
    expression = expression.replace(' ','')
    if not all(char in allowed_chars for char in expression):
        return "Error: Invalid characters in expression"
    else:
        y = eval(expression)
        return f"eval: {y}"
            
while True:
    x = input("Enter your operation: ")
    print(func(x))