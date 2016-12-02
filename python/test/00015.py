#!/usr/bin/python
#-*- coding:utf-8 -*-

#author	: Jollen Wang
#date	: 2016/05/10
#version: 1.0

'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

def main():
    score = int(raw_input("$>Enter the score:"))
    print "grade=",
    if score >= 90:
        print "A"
    elif score >= 60:
        print "B"
    else:
        print "C"

if __name__ == "__main__":
    main()


