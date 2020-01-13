#This program writes data to file1.txt and copy the data from file1.txt to file2.txt

with open("file1.txt","w+", encoding = "utf-8") as file:
    li = ["1Rivet ", "is ", "in ","valsad\n"]
    file.writelines("hello,\n")
    file.writelines("I am Deepak\n")
    file.writelines("1Rivet\n")
    file.writelines(li)


with open("file1.txt","r+", encoding = "utf-8") as file:
    # lines=file.readlines()
    # print(lines)

    for x in file:
        print(x)
    with open("file2.txt","w",encoding="utf-8") as file2:
        file2.writelines(lines)