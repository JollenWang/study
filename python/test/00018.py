#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
'''
def main():
    while True:
        a = raw_input("$>input 2 numbers split by ' ':").split(" ")
        if len(a) != 2:
            print("Please input 2 numbers!")
            continue

        num = int(a[0])
        if num > 9:
            print("out of range,input again!")
            continue
        break

    count = int(a[1])
    print("seed=%d,count=%d" %(num, count))
    total = 0
    last = 0
    print "$>total=",
    for i in range(1, count + 1):
        this = last * 10 + num
        last = this
        total += this
        if i == count:
            print(this)
        else:
            print("%d +" %this),
#        print("b=%d,l=%d,t=%d" %(base, last, total))

    print"$>sum=", total





main()
