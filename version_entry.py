from tkinter import *

count = 0
def click():
    global count
    mylabel = Label(root, text=e.get())
    mylabel.grid(row=count)
    count = count + 1


root = Tk()



root.geometry("1000x800")
root.title("To-do")
label = Label(root, text="My To-Do List", font=("Arial", 18))
label.grid(row=count)
count = count + 1

e = Entry(root, width=40, borderwidth=20)
e.grid(row=count)
count = count + 1

e.insert(0, "Enter a thing to-do: ")
button = Button(root, text="First button", command=click, fg="green", bg="yellow")
button.grid(row=count)
count = count + 1

# textbox = Text(root, font=("Arial", 16))
# textbox.pack()

root.mainloop()