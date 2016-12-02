#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：打印出如下图案（菱形）
 
    *
   ***
  *****
 *******
  *****
   ***
    *
'''

for s in range(6, 0, -2):
    print ' '*(s / 2) + '*' * (1 + (3 - s / 2) * 2)
for s in range(0, 6 + 1, 2):
    print ' '*(s / 2) + '*' * (1 + (3 - s / 2) * 2)
