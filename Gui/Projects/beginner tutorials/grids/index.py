import tkinter
from tkinter import *

#! Instantiate and Window Title
window = Tk()
window.geometry("420x420")
window.title("Title")

#* code starts below here:

# grid() = geometry manager that organizes widgets in a table-like structure in a parent container.


#! GRID TABLE
"""
*       |    column 0     |    column 1      |     column 2    |
* _____________________________________________________________|  ---->
*       |                 |                  |                 |
* row 0 |  (r=0, c=0)     |   (r=0, c=1)     |     (r=0, c=2)  |
*       |                 |                  |                 |
* _____________________________________________________________|  ---->
*       |                 |                  |                 |
* row 1 |  (r=1, c=0)     |   (r=1, c=1)     |     (r=1, c=2)  |
*       |                 |                  |                 |
* _____________________________________________________________|  ---->
*       |                 |                  |                 |
* row 3 |  (r=3, c=0)     |   (r=3, c=1)     |     (r=3, c=2)  |
*       |                 |                  |                 |
* _____________________________________________________________|  ---->
*
*       |                  |                 |
*       v                  v                 v

"""



# firstNameLabel = Label(window, text="First Name: ").pack()
# firstNameEntry = Entry(window).pack()
    # what if we want to place the label at the left side alighnment and entry box at the right hand side.
    
titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)
    
# grid
firstNameLabel = Label(window, text="First Name: ", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

#adjust row to avoid overlapping
lastNameLabel = Label(window, text="Last Name: ", bg="green").grid(row=2, column=0) 
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email: ", bg="blue", width=30).grid(row=3, column=0) 
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text='submit').grid(row=4, columnspan=2)

#! Display
window.mainloop()