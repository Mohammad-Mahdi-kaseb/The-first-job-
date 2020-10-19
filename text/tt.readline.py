with open("test.txt" , "r") as file:
    while True:
        line = file.readline()
        print(line)
        if line == "":
            break
print("Somthing breaked")        