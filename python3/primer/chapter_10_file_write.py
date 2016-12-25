#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

contex = """Hello Jollen,
Good luck at 2017!
"""

if __name__ == "__main__":
    f = open("info.txt", "w")
    f.writelines(contex)
    f.close()
