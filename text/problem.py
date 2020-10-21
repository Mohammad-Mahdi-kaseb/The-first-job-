with open("database.bat" , "r") as data:
 with open("new.txt" , "w") as nw:
    while True :
        line = data.readline()
        if line.startswith("wget"):
            nw.write(line.split()[3].strip("'")+"\n")
        if line == "" :
            break