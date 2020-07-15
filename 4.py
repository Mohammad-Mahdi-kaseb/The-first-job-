import tkinter as tk
from datetime import datetime


def turn():

    d = datetime.now()
    l1.config(text= d.strftime("%B-%d-%Y"),)
    s1.config(text= d.strftime("%I-%M-%S %p"))
    r1.config(text= d.strftime("%A"))
    numbers.append(len(numbers)+1)
    print(numbers)
    a1.config(text=numbers[-1])
root = tk.Tk()
numbers = []

tp = tk.Toplevel()




l1=tk.Label(root,text="",fg="red",bg="black")
l1.grid()

s1=tk.Label(root , text="")
s1.grid(row= 0 , column=0)

r1=tk.Label(root , text="")
r1.grid(row= 1 , column=0)

a1 =tk.Label(root , text="")
a1.grid(row= 2 , column=0)

b1 =tk.Button(root,text="get turn" , command=turn)
b1.grid(row= 3 , column=0)











root.mainloop()