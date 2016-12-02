#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序27】 
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

def reverse_output(str, len):
    if len == 0:
        return

    print s[len -1],
    reverse_output(str, len - 1)

s = raw_input("$>Enter a string:")
reverse_output(s, len(s))

