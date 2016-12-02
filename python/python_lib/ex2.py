#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
使用apply函数传递关键字参数
'''

def fun(a, b):
    print a, b

apply(fun, ("Good",), {"b": "Luck!"})
apply(fun, (), {"a": "Good", "b": "Luck!"})
