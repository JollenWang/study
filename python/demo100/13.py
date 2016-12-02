#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
'''

def declen(n):
    return len("%d" %n)

def flower(start, end):
    while True:
        start = int(raw_input("Enter start number:"))
        end = int(raw_input("Enter end number:"))
        try:
            declen(start) == 3 and declen(end) == 3
            print("dlen=%d,%d" %(declen(start), declen(end)))
            break
        except ValueError:
            print("Input is invalid number!\n")
 
    print("The Narcissus numbers between %d and %d are:\n" %(start, end))
    for n in range(start, end + 1):
        b = n / 100
        s = (n % 100) / 10
        g = n % 10
        if b*b*b + s*s*s + g*g*g == n:
            print(n)

a = 0
b = 0
if __name__ == "__main__":
    flower(a, b)
