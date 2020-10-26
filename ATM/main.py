import tkinter as tk
import tkinter.ttk as ttk 
import hashlib
#import pygame 

def to_shal(password):
  return hashlib.sha1(password.encode("utf-8")).hexdigest()

def register():
    input_user =  form_user.get()
    input_pass =  to_shal(form_pass.get())
    form_user.set("")
    form_pass.set("")
    with open("users.txt" , "a") as file:
        file.write(f"User:{input_user}Password:{input_pass}\n")
def login():
  pass

br = {"bg" : "#2c3e50"}
bt = {"bg" : "#f1c40f", }

#def play():
 #   pygame.mixer.music.load("Welcome sound effect.mp3")
  #  pygame.mixer.music.play()

root = tk.Tk()

#root.iconbitmap('Graphicloads-Flat-Finance-Atm.ico')
root.title("ATM")
root.minsize(200 , 200)
root.resizable(0 , 0)
root.config(br)
#pygame.mixer.init()
# top = tk.Toplevel()

note = ttk.Notebook()

register_form = tk.Frame()
register_form .config(bt)
login_form = tk.Frame()
login_form .config(bt)
note.add(register_form , text ="Register" )

note.add(login_form , text ="Log In" )

note.grid(row = 0 , column = 0 )
######## Register ############
form_user = tk.StringVar()
form_pass = tk.StringVar()
tk.Label(register_form , text = "User:", cnf=bt ,font = "Times"  ).grid(row=0 , column=0)
tk.Entry(register_form , textvariable=form_user).grid(row=0 , column= 1 )
tk.Button(register_form , text= "Register" , command = register).grid(row = 3 , column=0 , columnspan=2 , sticky=tk.W)
tk.Label(register_form , text = "Pasword:" , cnf=bt ,font = "Times"   ).grid(row=1 , column=0)
tk.Entry(register_form , textvariable=form_pass, show="*").grid(row=1 , column= 1 )
tk.Button(register_form , text= "Cancel" , command = root.destroy).grid(row = 3 , column=1 , columnspan=2 , sticky=tk.E)
tk.Button(register_form , text= "PLAY(movaghat)").grid(row = 4 , column=0 , columnspan=2 , sticky=tk.W+tk.E)

###### LOG IN ###########
tk.Label(login_form , text = "User:" ).grid(row=0 , column=0)
tk.Entry(login_form).grid(row=0 , column= 1 )
tk.Button(login_form , text= "Register").grid(row = 3 , column=0)
tk.Label(login_form , text = "Pasword:" ).grid(row=1 , column=0)
tk.Entry(login_form , show="*").grid(row=1 , column= 1 )
tk.Button(login_form , text= "Cancel", command = root.destroy).grid(row = 3 , column=1 , columnspan=2 , sticky=tk.E)
root.mainloop()