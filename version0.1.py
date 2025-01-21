import tkinter as tk

root = tk.Tk()

root.geometry("1000x800")
root.title("Workout UI")
label = tk.Label(root, text="My Workout Plan", font=("Arial", 18))
label.pack()

textbox = tk.Text(root, font=("Arial", 16))
textbox.pack()

root.mainloop()