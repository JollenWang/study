#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

import string

def main():
    str = raw_input("$>Enter a string:")
    letters = 0
    space = 0
    digit = 0
    others = 0

    for c in str:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print("#>There are %d letters, %d spaces, %d digits, %d others.\n" \
            %(letters, space, digit, others))

if __name__ == "__main__":
    main()
