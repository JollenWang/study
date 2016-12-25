#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

fname = "./info.txt"

if __name__ == "__main__":
    fd = open(fname, "r")
    contents = fd.read()
    words = contents.split()
    num = len(words)
    print(fname + " has %d words." %num)


