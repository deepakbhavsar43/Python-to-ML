# This program reads lines from a file and print all the special symbol present in that file

li = ["!","@","#","$","%","^","&","*","(",")","_","+"]
with open("symbols.txt","r+", encoding = "utf-8") as file:
    lines = file.readlines()
    # print(lines)
    for i in lines:
        for j in i:
            if j in li:
                print(j)