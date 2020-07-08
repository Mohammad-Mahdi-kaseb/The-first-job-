import tkinter as tk 



def lahze():
    print(1)


root = tk.Tk()

T = tk.Label(root, text="HI")
T.pack() 

L = tk.Button(root, text="Get Turn!",command="turn")
L.pack()

root.mainloop()