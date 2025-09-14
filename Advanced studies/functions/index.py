"""

    ! functions

"""

#! in python to define a function we use the keyword 'def'

#! example:
def my_function():
    print("Hello from a function")
    
#* to call a function, use the function name followed by paranthesis.
my_function()


#! Arguments:
#* information can be passed into functions as arguments.
#* arguments are specified after the function name, inside the paranthesis. You can add
#* as many as argumetns as you want, just separate them with a comma.

#! example:
def getName(fname, lname):
    print(f"Hello {fname} {lname}")
getName("John", "Doe") #* the passed arguments must be aligned with the function's parameters.
getName("Linus", "Torvalds")
getName("Mike", "Tyson")

#* when calling a function with an argument, it must meet the exact number of arguments passed in it, 
#* or else it will be an error.
# def exampleFunc(args1, args2):
#     print(f"welcome {args1} {args2}")
# exampleFunc("args 1") #* this will throw an error as it did not meet the exact arguments.



#! Arbitrary argumens, *args :
#* if you do not know how many arguments that will be passed into your function, add a * before the parameter name
#* in the function definition

#* this way the function will reveive a tuple of arguments, and can access the items accordingly:

def myFunc(*adults):
    print(f"The oldest is {adults[2]}")
myFunc("Emil", "Tobias", "Linus") #* this prints "The oldest is linus"



#! Keyword Arguments, key = value :
#* you can also send arguments with the  syntax

#* this way the order of the argumetns does not matter

def myF(child3, child2, child1):
    print(f"The youngest child is {child3}")
myF(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




#! Arbitrary Keyword Arguments, **kwargs
#* if you do not know how many keyword arguments that will be passed into your function, add two asterisk **
#* before the parameter name in the function definition.

#! example:
#* if the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_Func(**kid):
    print(f"His last name is {kid["lname"]}")
my_Func(fname="Tobias" , lname="Refsnes")



#! Default Parameter Value:
#* the following example shows how to use a default parameter value.
#* if we call the function without argument, it uses the default value.

def m_func(country = "Norway"):
    print(f"I am from {country}")
m_func("Sweden")
m_func("India")
m_func()
m_func("Brazil")


#! Passing a List as an Argument:
#* You can send any data types of argument to a function (string, number, list, dictionary etc.),
#* and it will be treated as the same data type inside the function.

#* e.g, if you send a List as an argument, it will still be a List when it reaches the function:

def pass_List(food):
    for x in food:
        print(x, end=" ")
    print()
fruits = ["apple", "banana", "cherry"]
pass_List(fruits)


#! Return Values
#* To let a function return a value, use the return statement:

def returnStatement(x):
    return 5 * x
print(returnStatement(3))
print(returnStatement(5))
print(returnStatement(9))


#! The pass Statement:
#* Function definitions cannot be empty, but if you for some reason have a function definition
#* with no content, put it in the pass statement to avoid getting an error.

def passFunc():
    pass


#! Positional-Only Arguments
#* You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#* To specify that a function can have only positional arguments, add, '/' after the arguments.

def ONLY_func(x, /):
    print(x)
ONLY_func(3)

#* without the , / you are actually allowed to use keyword arguments even if the function expects
#* positional arguments.
def onlyFunc(x):
    print(x)
onlyFunc(x = 3)

#* but when adding the , / you will get an error if you try to send a keyword argument
# def oF(x, /):
#     print(x)
# oF(x = 3)


#! Keyword-Only Arguments :
#* To specify that a function can only have keyword argumetns add '* ,' before the arguments.

def keywwordOnly_Func(*, x):
    print(x)
keywwordOnly_Func(x = 3)


#* without the *, you are allowed to use positional arguments even if the function expects keyword arguments.
def keywwordOnly_Func(x):
    print(x)
keywwordOnly_Func(3)

#* but with the *,  you will get an error if you try to send a positional argument.
# def keywwordOnly_Func(*, x):
#     print(x)
# keywwordOnly_Func(3)


#! Combine Positional-Only and Keyword-Only :
#* You can combine the two argument types in the same function.
#* any argument before the /, are positional only, and any argument after the *, are keyword only.

def mixOnly(a,b , /, *, c, d):
    print(a + b + c + d)
mixOnly(5, 6, c=7, d=8)