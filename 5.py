import tkinter as tk


root = tk.Tk()
####################################################################################################
#########TIMER##########                                                                           #
l_timer = tk.StringVar()                                                                           #
l_timer.set("20:00")                                                                               #
r_timer = tk.StringVar()                                                                           #
r_timer.set("20:00")                                                                               #
####################################################################################################
tk.Label(root, text="Left player", font=("times", 15,)).grid(row=0, column=0)                      #
tk.Label(root, text="Right player", font=("times", 15,)).grid(row=0, column=2, sticky=tk.N + tk.E) #
####################################################################################################
tk.Label(root, textvariable=l_timer).grid(row=1, column=0)                                         #
                                                                                                   #
tk.Label(root, textvariable=r_timer).grid(row=1, column=2)                                         #
####################################################################################################
tk.Button(root, text="stop", bg="red", font=("times", 15,),).grid(row=2, column=0)                 #
tk.Button(root, text="stop", bg="red", font=("times", 15,)).grid(row=2, column=2)                  #
tk.Button(root, text="start", bg="green", font=("times", 15,)).grid(row=3, column=1)               #
tk.Button(root, text="cancel", bg="yellow", font=("times", 15,)).grid(row=4, column=1)             #
####################################################################################################
root.mainloop()                                                                                    #
####################################################################################################