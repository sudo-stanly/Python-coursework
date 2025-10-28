
#! to create a class
class MyClass:
    x = 5
    
print(MyClass) #* output: <class '__main__.MyClass'>


#! create object
#* now we can use the class named MyClass to create objects:
# example: Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x) #* output: 5



#! delete objects
#* you can delete objects by using the 'del' keyword
# example: Delete the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is"+self.name)

p1 = Person("Torvalds", 36)

del p1
print(p1) #* output: NameError: name 'p1' is not defined



#! multiple objects:
# you can create multiple objects from the same class:
p1 = MyClass()
