#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''

from math import sqrt

def main():
    for i in range(101, 201):
        flag = True;
        k = int(sqrt(i))
        for j in range(2, k + 1):
            if i % j == 0:
                flag = False;
                break

        if flag == True:
            print("Found prime:%d" %i)

if __name__ == "__main__":
    main()




