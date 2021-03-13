import tkinter as tk

root = tk.Tk()
root.title("The Calculator")
root.geometry("500x500")

#-----------------------------Option Box Thing-----------------------------
modes = ["Arithmetic", "Physics", "Calculus"]

default_mode = tk.StringVar()
default_mode.set(modes[0])

calc_mode = tk.OptionMenu(root, default_mode, *modes).pack()

#-----------------------------Input Fields-----------------------------
default_input1 = tk.IntVar()
default_input2 = tk.IntVar()

default_input1.set(0)
default_input2.set(0)

input1 = tk.Entry(root, text=default_input1)
input2 = tk.Entry(root,  text=default_input2)

input1.pack()
input2.pack()

#-----------------------------Button-----------------------------
def butt_solve():
    num1 = input1.get()
    num2 = input2.get()
    total = int(num1) + int(num2)
    answer_label.config(text=f"Answer: {total}")
    test_label.config(text=default_mode.get())

butt = tk.Button(root, text="Calculate", command=butt_solve)
butt.pack()
#-----------------------------Label-----------------------------
answer_label = tk.Label(text="Answer: ")
answer_label.pack()

test_label = tk.Label(text=default_mode.get())
test_label.pack()

# root.resizable(False, False)
root.mainloop()