import tkinter as tk 
import tkinter.ttk as ttk


# ################food information ##################### #

i = {
    "1" : {"name" :"Akbar Chicken",
          "rating" : 5 , 
          "review" : 47 ,
          "price" : 2.58 } 
}

# ######################### Master ##################### #
bgak = {"bg" : "#00897B"}
bgak1 = {"bg" : "#FF5722" ,"font":'Helvetica'}
bgak2 = {"bg" : "#CDDC39" ,"font":'Helvetica'}
bgak3 = {"bg" : "#FF9800" ,"font":'Helvetica'}


root =tk.Tk()

root.title("ᴀᴋʙᴀʀ ᴄʜɪᴄᴋᴇɴ")


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

name = i["1"]["name"]
tk.Label(food1, text = name, cnf=bgak1 ).grid(row = 0 , column = 0 , pady = 5 , padx = 5 )

rating = i["1"]["rating"] * "★" + "(" + str(i["1"]["review"]) + ")"
tk.Label(food1, text = rating, cnf=bgak2 ).grid(row = 1 , column = 0 , pady = 5)

price = str(i["1"]["price"]) + "$"
tk.Label(food1, text = price , cnf=bgak3 ).grid(row = 2 , column = 0 , pady = 5 )



root.mainloop()