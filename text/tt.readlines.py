with open("test.txt" , "r") as file:
    while True:
        line = file.readlines()
        print(line[2])
               