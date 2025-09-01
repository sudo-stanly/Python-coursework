import tkinter
from tkinter import *
from tkinter import messagebox #* import message box library

#! Instantiate and Window Title
window = Tk()
window.geometry("420x420")
window.title("Title")

#* code starts below here:

def click():
    
    #* info messagebox
    # messagebox.showinfo(title='this is a info message box' ,message='Hello world')
    
    #* warning messagebox
    # messagebox.showwarning(title='warning' ,message='Storage is running out!')
    
    #! warning message box in a loop
    # while True:
    #     messagebox.showwarning(title='warning' ,message='Storage is running out!')
    
    #* error messagebox
    # messagebox.showerror(title='error' ,message='Something went wrong!')
    
    
    
    #! sophisticated message boxes (boolean types)
    #* ask ok cancel messagebox
    # if messagebox.askokcancel(title='ask ok cancel' ,message='Do you want to study?'):
    #     print("You did it!")
    # else:
    #     print("Try again :(")
    
    #* ask retry cancel messagebox
    # if messagebox.askretrycancel(title='ask ok cancel' ,message='Do you want to retry?'):
    #     print("You did it!")
    # else:
    #     print("Try again :(")
    
    #* ask yes or no messagebox
    # if messagebox.askyesno(title='ask yes or no' ,message='Do you like cake?'):
    #     print("I like cake too")
    # else:
    #     print("Why do you not like cake?")
    
    #* ask question messagebox (this returns a string of yes or no)
    # print(messagebox.askquestion(title='ask question' ,message='Do you like pie?'))
    # answer = messagebox.askquestion(title='ask question' ,message='Do you like pie?')
    # if answer == 'yes':
    #     print("I like pie too!")
    # else:
    #     print("Why do you not like pie?")
    
    #* yes no cancel
    # print(messagebox.askyesnocancel(title='ask yes no cancel' ,message='Do you like to code?'))
    # answer = messagebox.askyesnocancel(title='ask yes no cancel' ,message='Do you like to code?')
    # if answer == True:
    #     print("You like to code")
    # elif answer == False:
    #     print("why not?")
    # else:
    #     print("You have dodged the question")
    
    #* change messagebox icon
    answer = messagebox.askyesnocancel(title='ask yes no cancel' ,message='Do you like to code?', icon='error') #! icons: warning, info, error
    if answer == True:
        print("You like to code")
    elif answer == False:
        print("why not?")
    else:
        print("You have dodged the question")
        
button = Button(window, command=click,text='click me')
button.pack()


#! Display
window.mainloop()