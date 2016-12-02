#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序26】 
 题目：利用递归方法求5!。
'''

def fun(i):
    if i == 0:
        return 1
    return i * fun(i - 1)

print("fun(0)=%d" %fun(0))
print("fun(1)=%d" %fun(1))
print("fun(5)=%d" %fun(5))

