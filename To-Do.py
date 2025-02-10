from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("To-Do Application")
to_do = LabelFrame(root, text="To-Do Part", padx=10, pady=10)
to_do.pack(padx=20, pady=20)

label = Label(to_do, text="This the part that we add the things")
label.pack()


mainloop()