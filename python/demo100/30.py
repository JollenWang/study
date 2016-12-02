#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序30】
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　　　
'''

def check_num(n):
    if n < 10000 or n > 99999:
        print("Invalid number %d!" %n)
        return -1

    i = str(n)
    for j in range(0, 2):
        if i[j] != i[4 - j]:
            return 0
    return 1

res = ['NO', 'YES']
while True:
    num = int(raw_input("$>Enter a 5-bits number:"))
    ret = check_num(num)
    if ret >= 0:
        print res[ret & 1]
        break
