#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序29】 
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''

def foo(n, c):
    if n == 0:
        print("\r\n$>is a %d bits number." %c)
        return
    print n % 10,

    n /= 10
    c += 1
    foo(n, c)

n = int(raw_input("$>Enter a number:"))
foo(n, 0)






