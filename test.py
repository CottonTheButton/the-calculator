import tkinter as tk

root = tk.Tk()

clicked = tk.StringVar()
clicked.set("Math")

drop = tk.OptionMenu(root, clicked, "Physics", "CHemistry", "Math")
drop.pack()

root.mainloop()