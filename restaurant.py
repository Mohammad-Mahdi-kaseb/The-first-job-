import tkinter as tk 
import tkinter.ttk as ttk



# ######################### Master ##################### #
bgak = {"bg" : "#00897B"}
bgak1 = {"bg" : "#FF5722" ,"font":'Helvetica'}


root =tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)


food = tk.Frame() 

drinks = tk.Frame()

rescipt = tk.Frame()

note.add(food , text = "FOOD")
note.add(drinks , text = "DRINKS")
note.add(rescipt , text = "RESCIPT")



food1 = tk.Frame(food , cnf=bgak )
food1.grid(row = 0 , column = 0 , sticky = tk.E+tk.W)
# tk.LabelFrame(food1 , text = "IRANIN FOOD ").grid(row = 0 , column = 0)
tk.Label(food1, text = "Akbar Chicken", cnf=bgak1 ).grid(row = 0 , column = 0 , pady = 5 , padx = 5 )
tk.Label(food1, text = "★★★★", cnf=bgak ).grid(row = 1 , column = 0)
tk.Label(food1, text = "2.6$", cnf=bgak ).grid(row = 2 , column = 0)



root.mainloop()