#!/usr/bin/python

# Script for manage and update documents

import sys
import os

SRC_DIR = "D:\\workspace\\backup"
DST_DIR = os.getcwd()

print("SRC_DIR=", SRC_DIR)
print("DST_DIR=", DST_DIR)

def getFileList(path):
    p=str(path)
    if p=="":
        print("Null input!")
        return []

    p=path.replace("/", "\\")
    if p[-1]!="\\":
        p+="\\"

    a=os.listdir(p)
    b=[x for x in a if os.path.isfile(p+x)]
    return b

print(getFileList("C:\\"))

