from tkinter import *

root = Tk()

def callback(event):
    print("KEY")

frame = Frame(root)
frame.bind("<Key>", callback)
frame.pack()

root.mainloop()