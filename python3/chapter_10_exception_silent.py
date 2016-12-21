#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

if __name__ == "__main__":
    fname = input("Input file name:")
    try:
        fd = open(fname, 'r')
    except FileNotFoundError:
        pass
    else:
        contents = fd.read()
        fd.close()
        print("%s's content:" %fname)
        print(contents.rstrip())

