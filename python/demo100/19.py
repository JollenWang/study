#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　找出1000以内的所有完数。
'''

from math import sqrt

def check_full_num(n):
    sum = 0
    k = int(sqrt(n))
#    print("sqrt(%d)=%d" %(n, k))

    for i in range(1, k + 1):
        if n % i == 0:
            sum += n / i
            sum += i
#    print("sum=%d" %sum)

    if sum == 2 * n:
        return 1
    else:
        return 0

def check_input():
    while True:
        n = int(raw_input("$>Enter a number in range of 1 ~ 1000:"))
        if n > 0 and n < 1001:
            break
    str = "YES" if check_full_num(n) else "NO"
    print(str)
    print("%d %s a full number!" %(n, "is" if check_full_num(n) else "isn't"))

def main():
    print("$>Find out all the 'full number' in range 1 ~ 1000:")
    for i in range(1, 1001):
        if check_full_num(i) == 1:
            print("#>%d is full number!" %i)

check_input()
main()
