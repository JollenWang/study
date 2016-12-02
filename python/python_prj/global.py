#!/usr/bin/python

#demo function for global variables

def global_var():
    #global X;
    X = 0;
    print('X old=',X);
    X = 15;
    print('change X to', X);


X=100;
global_var();
print('X new=', X);