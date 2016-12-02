#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序24】 
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
'''
def get_sum():
    n = 2.0
    d = 1.0
    sum = 0

    print'sum=',
    for i in range(0, 20):
        this = n / d
        n += d
        d = n - d
        sum += n/d
        if i == 19:
            print('%d/%d' %(n, d))
        else:
            print('%d/%d+' %(n, d)),
        
    print("$Total=%f" %sum)

if __name__ == "__main__":
    get_sum()
