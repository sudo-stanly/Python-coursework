import tkinter
from tkinter import *

#! Instantiate and Window Title
window = Tk()
#window.geometry("420x420")
window.title("Title")

#* code starts below here:

def submit():
    username = entry.get() #* this retrieves the text we entered and stores it within the variable username.
    print("Hello ",username)
    
def delete():
    entry.delete(0, END) #* deletes the line of text
    
def backspace():
    entry.delete(len(entry.get())-1, END) #* deletes last character

#* submit button
submit = Button(window, text='submit', command=submit)
submit.pack(side = RIGHT) #* places button to the right

#* delete button
delete = Button(window, text='delete', command=delete)
delete.pack(side = RIGHT) #* places button to the right

#* backspace button
backspace = Button(window, text='backspace', command=backspace)
backspace.pack(side = LEFT) #* places button to the right

# entry widget = textbox that acepts a single line of user input
entry = Entry()                          #* input
entry.config(font=('Sans serif', 50))
entry.config(bg='#000000')
entry.config(fg='#00ff00')              
#entry.insert(0,'Enter something')        #* default text
#entry.config(state=DISABLED)             #* state ACTIVE/DISABLED
entry.config(width=10)                    #* size of the entry box
#entry.config(show='*')                    #* this will hash or hide what you input on the entry (does not have to be an asterisk)

entry.pack()                              #* display entry

#! Display
window.mainloop()