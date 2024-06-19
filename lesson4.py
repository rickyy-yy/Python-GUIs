from tkinter import *

# Creating root widget
root = Tk()

entry = Entry(root, width=50)
entry.pack()
entry.insert(0, "Enter your name")


def on_click():  # Function to run when button is clicked
    text = entry.get()
    myLabel = Label(root, text=f"{text}")
    myLabel.pack()

# Creates a button with "Click Me!" text
myButton = Button(root, text="Enter Name!", command=on_click, fg='blue', bg='#9999FF')

# Packs the button into the GUI
myButton.pack()

# Starts the GUI
root.mainloop()
