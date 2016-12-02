#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序28】 
题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
'''

def calc_age(i):
    if i == 1:
        return 10
    return calc_age(i - 1) + 2

n = int(raw_input("$>input a number:"))
print("$>The %dth person's age is %d" %(n,calc_age(n)))
