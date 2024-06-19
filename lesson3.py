from tkinter import *

# Creating root widget
root = Tk()


def on_click():  # Function to run when button is clicked
    myLabel = Label(root, text="Clicked")
    myLabel.pack()

# Creates a button with "Click Me!" text
myButton = Button(root, text="Click Me!", command=on_click, fg='blue', bg='#9999FF')

# Packs the button into the GUI
myButton.pack()

# Starts the GUI
root.mainloop()
