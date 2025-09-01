import tkinter
from tkinter import *

#! Instantiate and Window Title
window = Tk()
window.geometry("420x420")
window.title("button")

#* code starts below here:

count = 0
def click():
    #print("Hello world")
    global count
    count+=1
    #print(count)
    label.config(text=count)
    label2.pack()

button = Button(window, text='Click me!!!')
button.config(command=click) #* when writing a button command make a function and add it here exluding the parenthesis of the function passed to the Button function.
                             #* performs callback of a function
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#e85313')
button.config(fg='#e8cf13')

button.config(activebackground='#FF0000') #* changing active state of the button background
button.config(activeforeground='#e8cf13') #* changing active state of the button foreground

image = PhotoImage(file='./Gui/Projects/beginner tutorials/button/logo.png')
button.config(image=image)
button.config(compound='top') #* (top/bottom/right/left)

#button.config(state=ACTIVE) #* (state=ATIVE/DISABLED)

#display count on window
label = Label(window, text=count)
label.config(font=('Monospace', 50))
label.pack()

label2 = Label(window, image=image)

button.pack()

#! Display
window.mainloop()