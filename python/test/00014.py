#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

def main():
    n = int(raw_input("$>input a number:"))
    print n,"=",
    while(n != 1):
        for i in range(2, n + 1):
            if (n % i) == 0:
                n /= i
                if (n == 1):
                    print "%d" %i
                else:
                    print "%d * " %i,
                break

if __name__ == "__main__":
    main()
