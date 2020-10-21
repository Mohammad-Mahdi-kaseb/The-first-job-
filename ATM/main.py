import tkinter as tk
import tkinter.ttk as ttk 




root = tk.Tk()

# top = tk.Toplevel()

note = ttk.Notebook()

register_form = tk.Frame()

login_form = tk.Frame()

note.add(register_form , text ="Register" )

note.add(login_form , text ="Log In" )

note.grid(row = 0 , column = 0 )
######## Register ############
form_user = tk.StringVar()
form_pass = tk.StringVar()
tk.Label(register_form , text = "User:" ).grid(row=0 , column=0)
tk.Entry(register_form , textvariable=form_user).grid(row=0 , column= 1 )
tk.Button(register_form , text= "Register").grid(row = 3 , column=0)
tk.Label(register_form , text = "Pasword:" ).grid(row=1 , column=0)
tk.Entry(register_form , textvariable=form_pass).grid(row=1 , column= 1 )
tk.Button(register_form , text= "Cancel").grid(row = 3 , column=1 , columnspan=2 , sticky=tk.E)

###### LOG IN ###########
tk.Label(login_form , text = "User:" ).grid(row=0 , column=0)
tk.Entry(login_form).grid(row=0 , column= 1 )
tk.Button(login_form , text= "Register").grid(row = 3 , column=0)
tk.Label(login_form , text = "Pasword:" ).grid(row=1 , column=0)
tk.Entry(login_form).grid(row=1 , column= 1 )
tk.Button(login_form , text= "Cancel").grid(row = 3 , column=1 , columnspan=2 , sticky=tk.E)
root.mainloop()