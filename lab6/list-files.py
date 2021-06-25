#!/usr/bin/env python
import os


files = os.listdir(os.curdir)
print(files)

print("***********print dirs only*****************")


for file in files:
    if os.path.isdir(file):
        print(file)



print("***********print dirs and subdirs only*****************")

for file in files:
    if os.path.isdir(file):
        print(file)
        for sub in os.listdir(file):
            print(file)


def recursive(file):
    if os.path.isdir(file):
        print(file)
        for sub in os.listdir(file):
            #print(sub)
            if os.path.isdir(sub):
                recursive(os.path.join(file,sub))
            else:
                continue
    else:
        return

print("***********recursive dirs*****************")

recursive(os.curdir)
