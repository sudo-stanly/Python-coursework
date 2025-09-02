import tkinter
from tkinter import *

#! Instantiate and Window Title
window = Tk()
window.geometry("420x420")
window.title("Title")

#* code starts below here:

# frame = a rectangular container to group and hold widgets.

# create frame
frame = Frame(window, bg='pink', bd=5, relief=SUNKEN)
#frame.pack(side=BOTTOM) # display frame
# frame.place(x=0, y=0)

# replace window as frame
Button(frame, text='w', font=('Consolas', 25), width=3).pack(side=TOP) # shortcut
Button(frame, text='a', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='s', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='d', font=('Consolas', 25), width=3).pack(side=LEFT)



#! Display
window.mainloop()