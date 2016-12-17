#!/usr/bin/python
#-*- coding:utf-8 -*-

#author : Jollen Wang
#date   : 2016/10/12
#version: 2.0

def r3d_print(task, done):
    while task:
        current = task.pop();
        print("Printing " + current + " ...")
        done.append(current)

def show_work(done):
    for i in done:
        print(i)

if __name__ == "__main__":
    task = ['iWatch', 'iPhone', 'Gun', 'Ship', 'Car']
    done = []
    r3d_print(task, done)
    show_work(done)




