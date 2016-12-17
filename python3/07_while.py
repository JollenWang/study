#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

while True:
    message = input("Input you command: ")
    if (message == 'Q' or message == 'q' or message == 'quit' or message == 'exit'):
        break;
    print("Command:", message)
print('end.')
