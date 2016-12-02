#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：输出9*9口诀。
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" %(j,i,i*j)),
    print("")
