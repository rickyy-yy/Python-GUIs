from tkinter import *

# Creating root widget
root = Tk()

# Creating a label widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="I have no name")

# Put first label at zeroth row and column
myLabel1.grid(row=0, column=0)

# Put second label at first row and zeroth column
myLabel2.grid(row=1, column=5)

# Starts the GUI
root.mainloop()
