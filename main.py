import tkinter as tk

root = tk.Tk()

myLabel1 = tk.Label(root, text="Hello, world!")
myLabel2 = tk.Label(root, text="Cotton!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()