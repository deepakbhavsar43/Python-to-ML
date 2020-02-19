import os

basepath = input("\nEnter directory name : ")
dir = os.walk(basepath)
fileList = []
dup_list = []


def joinPath(path, file):
    path = path + file
    return path


for path, subdirs, files in dir:
    # print(f"path : {path}\nsubdir : {subdirs}\nfiles : {files}\n")
    for file in files:
        temp = joinPath(path + '\\', file)
        fileList.append(temp)

length = len(fileList)
for i in range(0, length):
    with open(fileList[i], "r") as f1:
        for j in range(i + 1, length):
            with open(fileList[j], "r") as f2:
                f1.seek(0)
                if f1.readlines() == f2.readlines():
                    dup_list.append(fileList[j])

print(f"\nAll the duplicate files in the directory \"{basepath}\" are as listed below :\n")
for i, j in enumerate(dup_list, 1):
    print(f"({i})  {j}")