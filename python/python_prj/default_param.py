#!/usr/bin/python

#this is a program demo of default parameters

def talk(msg,count = 1):
    print('msg=', msg);
    msg = input('input a string:');
    print((msg +'\n') * count);


talk('Jollen\n');
talk('Happy!\n', 6);
