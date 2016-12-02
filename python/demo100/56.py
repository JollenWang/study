#!/usr/bin/env python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序56】
题目：画圆【Tkinter模块】
'''
import os, sys

if __name__ == "__main__":
    from Tkinter import *

    canvas = Canvas(width = 800, height = 600, bg = 'red')
    canvas.pack(expand = YES, fill = BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width = 1)
        k += j
        j += 0.3

    mainloop()

    







