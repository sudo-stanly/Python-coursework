import tkinter
from tkinter import *

#* widgets = GUI elements: buttons, textboxes, labels, images
#* windows = serves as a container to hold or contain widgets


# creating and customizing our own window.

window = Tk() #insantiate an instance of a window for us

#* customizing the window screen
window.geometry("420x450") #format (width x height)

#* disable resizing (fixed size window)
#window.resizable(False, False)  # (width, height)

#* Display
window.mainloop() #this will place window on computer screen, will also listen for events 