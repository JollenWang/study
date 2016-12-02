#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
【程序21】
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下
的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
#-----------------------------------------------
# algorithm 1
#-----------------------------------------------
n = 1
for i in range(9, 0, -1):
    n = (n + 1) << 1

print(n)

#-----------------------------------------------
# algorithm 2
#-----------------------------------------------
total = 0
orignal = 1

while True:
    x = orignal
    for i in range(1, 11):
        x /= 2
        if x < 1:
            break
        total += (x + 1)
        x -= 1

    if (i != 9) or (total != (orignal - 1)):
        orignal += 1
        total = 0
        continue
        
    print("Total=%d" %orignal)
    break
