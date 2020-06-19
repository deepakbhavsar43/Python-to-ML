import os


def joinPath(path, file):
    path = path + file
    return path


def readdir():
    fileList.clear()
    dir = os.walk(basepath)

    for path, subdirs, files in dir:
        # print(f"path : {path}\nsubdir : {subdirs}\nfiles : {files}\n")
        for file in files:
            temp = joinPath(path + '\\', file)
            fileList.append(temp)


if __name__ == "__main__":
    basepath = input("\nEnter directory name : ")
    # basepath = '1Rivet'
    fileList = []
    dup_list = []

    readdir()
    length = len(fileList)
    for i in range(0, length):
        with open(fileList[i], "r") as f1:
            for j in range(i + 1, length):
                with open(fileList[j], "r") as f2:
                    f1.seek(0)
                    if f1.readlines() == f2.readlines():
                        dup_list.append(fileList[j])

    for i in dup_list:
        os.remove(i)
    readdir()
    # print("-----------",after)
    print(f"\nAll the files in the directory \"{basepath}\" after deleting duplicates is listed below :\n")
    for i, j in enumerate(fileList, 1):
        print(f"({i})  {j}")

    print(f"\nAll the duplicate files deleted from the directory \"{basepath}\" are as listed below :\n")
    for i, j in enumerate(dup_list, 1):
        print(f"({i})  {j}")
