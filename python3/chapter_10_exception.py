#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

if __name__ == "__main__":
    a = int(input(">input first number:"))
    b = int(input(">input second number:"))
    try:
        c = a / b
    except ZeroDivisionError:
        print("You have divide by zero!")
    else:
        print("%d / %d = %f" %(a, b, c))
