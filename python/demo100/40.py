#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序40】
题目：将一个数组逆序输出。
'''
a = [1,2,3,4,5,6,7,8,9,0]
l = len(a)

print a
for i in range(l/2):
    a[i], a[l - 1 -i] = a[l - 1 - i], a[i]

print a







