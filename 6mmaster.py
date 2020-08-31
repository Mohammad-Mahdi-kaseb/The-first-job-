import tkinter as tk
import tkinter.ttk as ttk

def callback(arg1 , arg2 ,arg3):
    p1.set(e1.get())
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
patient1 = tk.LabelFrame(patient , text='Patient1')
patient1.grid(row = 0 , column = 0 , padx=10)

tk.Label(patient1, text = "NAME:").grid(row=0, column=0)
tk.Label(patient1, text = "TIME:").grid(row=1, column=0)
patient2 = tk.LabelFrame(patient , text='Patient2')
patient2.grid(row = 1 , column = 0 , padx=10)

tk.Label(patient2, text = "NAME:").grid(row=0, column=0)
tk.Label(patient2, text = "TIME:").grid(row=1, column=0)
patient3 = tk.LabelFrame(patient , text='Patient3')
patient3.grid(row = 2 , column = 0 , padx=10)

tk.Label(patient3, text = "NAME:").grid(row=0, column=0)
tk.Label(patient3, text = "TIME:").grid(row=1, column=0)

############################################
h_p_1 = tk.StringVar()
h_p_1.set("12")
m_p_1 = tk.StringVar()
m_p_1.set("59")
s_p_1 = tk.StringVar()
s_p_1.set("59")
f1 = tk.Frame(patient1)
f1.grid(row= 1 , column = 1)
tk.Spinbox(f1 ,
 from_ = 0 ,
  to = 23 ,
   wrap = True ,
    textvariable = h_p_1 ,
     width = 2 , 
     state = "readonly").grid(row = 0 , column = 0)
e1 = tk.StringVar()
e1.trace("w" , callback)
e2 = tk.StringVar()
e2.trace("w" , callback)
e3 = tk.StringVar()
e3.trace("w" , callback)

tk.Entry(patient1 ,textvariable = e1 ).grid(row = 0 , column = 1)

tk.Entry(patient2 ,textvariable = e2 ).grid(row = 0 , column = 1)

tk.Entry(patient3 ,textvariable = e3 ).grid(row = 0 , column = 1)

root.mainloop()