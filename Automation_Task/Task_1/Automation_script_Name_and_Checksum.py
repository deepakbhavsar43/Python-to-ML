import hashlib
import os

chkSum = []


def joinPath(path, file):
    path = path + file
    return path


def chksum(file):
    print(f"File name: {file}")
    print("checksum : ", hashlib.md5(open(file, 'rb').read()).hexdigest())


basepath = '1Rivet'
# basepath = input("\nEnter directory name : ")
dir = os.walk(basepath)
fileList = []

fileName = []

for path, subdirs, files in dir:
    # print(f"path : {path}\nsubdir : {subdirs}\nfiles : {files}\n")
    for file in files:
        temp = joinPath(path + '\\', file)
        fileList.append(temp)
        fileName.append(file)

for f in fileList:
    chksum(f)

# l = len(fileName)
# for i in range(0, l):
#     print(f"{fileName[i]} {fileList[i]}")
