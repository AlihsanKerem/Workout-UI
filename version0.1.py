from tkinter import *


def click():
    mylabel = Label(root, text="Coaa")
    mylabel.pack()

root = Tk()


root.geometry("1000x800")
root.title("To-do")
label = Label(root, text="My Workout Plan", font=("Arial", 18))
label.pack()
button = Button(root, text="First button", command= click)
button.pack()
# textbox = Text(root, font=("Arial", 16))
# textbox.pack()

root.mainloop()