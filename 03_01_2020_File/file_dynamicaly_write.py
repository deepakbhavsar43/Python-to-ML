li=[]
print("Enter lines to write in file : ")
for i in range(0,9):
    li.append(str(input()))

with open("dynamic_write.txt","w+",encoding="utf-8") as file:
    file.writelines(li)