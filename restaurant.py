import tkinter as tk 
import tkinter.ttk as ttk



# ######################### Master ##################### #


root = tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)


food = tk.Frame() 

drinks = tk.Frame()

rescipt = tk.Frame()

note.add(food , text = "FOOD")
note.add(drinks , text = "DINKS")
note.add(rescipt , text = "RESCIPT")

root.mainloop()