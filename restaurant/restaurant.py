import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import PhotoImage

# ################food information ##################### #

i = {
    "1" : {"name" :"Akbar Chicken",
          "rating" : 5 , 
          "review" : 47 ,
          "price" : 2.58,
          "img" : "restaurant/img/fd9e168e23ededfd719b7787fb3501ba.gif"} , 
    "2" : {"name" :"Mahi Polo",
          "rating" : 5 , 
          "review" : 47 ,
          "price" : 2.58,
          "img" : "restaurant/img/fd9e168e23ededfd719b7787fb3501ba.gif" } 
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

for b in range(len(i)):
    food1 = tk.Frame(food , cnf=bgak )
    food1.grid(row=b , column = 0 , sticky = tk.E+tk.W)

    name = i["1"]["name"]
    tk.Label(food1, text = name, cnf=bgak1 ).grid(row = 0 , column = 0 , pady = 5 , padx = 5 )

    rating = i["1"]["rating"] * "★" + "(" + str(i["1"]["review"]) + ")"
    tk.Label(food1, text = rating, cnf=bgak2 ).grid(row = 1 , column = 0 , pady = 5)

    price = str(i["1"]["price"]) + "$"
    tk.Label(food1, text = price , cnf=bgak3 ).grid(row = 2 , column = 0 , pady = 5 )


    img = PhotoImage(file =i["1"]["img"]).subsample(2)
    tk.Label(food1, image = img).grid(row = 0 , column = 1 , rowspan = 3 )


root.mainloop()