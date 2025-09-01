import tkinter
from tkinter import *

#! Instantiate and Window Title
window = Tk()
window.geometry("420x420")
window.title("Labels")

#* code starts below here:

#adding image in label
photo = PhotoImage(file='./Gui/Projects/beginner tutorials/labels/logo.png')

label = Label(
              window, 
              text="Hello world",           #* text to display in label
              font=('Arial', 40, 'bold'),   #* font style of the text
              fg='green',                   #* foreground of the text
              bg='black',                   #* background of the window
              relief=RAISED,                #* sunken or raised border line
              bd=10,                        #* border thickness
              padx=20,                      #* padding width
              pady=300,                     #* padding height
              #image=photo,                 #* photo in label
              compound='bottom'             #* this function modifies the placement of the text in label
            ) #! calling the Label function and formatting the label

label.pack() # this will display the label on the window by the center
# label.place(x=0, y=0) # modifying the position of the label



#! Display
window.mainloop()