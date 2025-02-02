from tkinter import *

root = Tk()

root.geometry("1000x800")
root.title("Workout UI")
label = Label(root, text="My Workout Plan", font=("Arial", 18))
label.pack()

textbox = Text(root, font=("Arial", 16))
textbox.pack()

root.mainloop()