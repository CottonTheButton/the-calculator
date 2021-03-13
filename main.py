import tkinter as tk

root = tk.Tk()
root.title("The Calculator")
root.geometry("200x150")

input1 = tk.Entry(root)
input2 = tk.Entry(root)

input1.pack()
input2.pack()

def butt_add():
    num1 = input1.get()
    num2 = input2.get()
    total = int(num1) + int(num2)
    lab.config(text=f"answer = {total}")
    

butt = tk.Button(root, text="Calculate", command=butt_add)
butt.pack()

lab = tk.Label(text="")
lab.pack()

root.mainloop()