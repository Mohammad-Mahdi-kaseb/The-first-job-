import tkinter as tk
import tkinter.ttk as ttk

def b1():
    pass




root = tk.Tk()
root.title("NURSE HELPING")
note = ttk.Notebook()
note.grid(row=0, column=0)

timer = tk.Frame()
patient = tk.Frame()

note.add(timer, text='Timer')
note.add(patient, text='Patient')

# ############### Timer First Row ############## #
p1 = tk.StringVar()
p1.set('T1')
tk.Label(timer, textvariable=p1).grid(row=0, column=0)
p2 = tk.StringVar()
p2.set('T2')
tk.Label(timer, textvariable=p2).grid(row=0, column=1)
p3 = tk.StringVar()
p3.set('T3')
tk.Label(timer, textvariable=p3).grid(row=0, column=2)
# ############### Timer First Row ############## #
l1 = tk.StringVar()
l1.set('00:00')
tk.Label(timer, textvariable=l1).grid(row=1, column=0)
l2 = tk.StringVar()
l2.set('00:00')
tk.Label(timer, textvariable=l2).grid(row=1, column=1)
l3 = tk.StringVar()
l3.set('00:00')
tk.Label(timer, textvariable=l3).grid(row=1, column=2)
# ############### Butten ############## #
tk.Button(timer , text = "SET" , command = b1 ).grid(row = 2 , column = 0)
tk.Button(timer , text = "SET" , command = b1 ).grid(row = 2 , column = 1)
tk.Button(timer , text = "SET" , command = b1 ).grid(row = 2 , column = 2)
tk.Button(timer , text = "CANCEL" , command = root.destroy  ).grid(row = 3 , column = 0 , columnspan = 3
 , sticky = tk.W+tk.E )
###########################################


tk.Label(patient, text = "1_NAME:").grid(row=0, column=0)
tk.Label(patient, text = "1_TIME:").grid(row=1, column=0)
tk.Label(patient, text = "2_NAME:").grid(row=2, column=0)
tk.Label(patient, text = "2_TIME:").grid(row=3, column=0)
tk.Label(patient, text = "3_NAME:").grid(row=4, column=0)
tk.Label(patient, text = "3_TIME:").grid(row=5, column=0)
############################################
e1 = tk.StringVar()
e2 = tk.StringVar()
e3 = tk.StringVar()
e4 = tk.StringVar()
e5 = tk.StringVar()
e6 = tk.StringVar()
tk.Entry(patient ,textvariable = e1 ).grid(row = 0 , column = 1)
tk.Entry(patient ,textvariable = e2).grid(row = 1 , column = 1)
tk.Entry(patient ,textvariable = e3).grid(row = 2 , column = 1)
tk.Entry(patient ,textvariable = e4 ).grid(row = 3 , column = 1)
tk.Entry(patient ,textvariable = e5 ).grid(row = 4 , column = 1)
tk.Entry(patient ,textvariable = e6 ).grid(row = 5 , column = 1)


root.mainloop()