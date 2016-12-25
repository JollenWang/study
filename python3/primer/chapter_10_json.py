#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

import json

number = [2, 3, 5, 7, 99]

if __name__ == "__main__":
    fd = open("num.json", "w")
    json.dump(number, fd)
    fd.close()

    num = json.load(open("num.json"))
    print(num)

