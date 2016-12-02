#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

numbers = []
while True:
    line = raw_input("input numbers:")
    if line:
        for n in line.split():
            try:
                numbers.append(int(n))
            except ValueError:
                print("#>%s is not number!" % n)
    else:
        break

print(numbers)
