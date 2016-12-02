#!/usr/bin/python

#demo for module

import sys

def using_sys():
    print('The command line arguments are:');
    for i in sys.argv:
        print(i);

    print('The PYTHONPATH is ', sys.path);


using_sys();

import using_name
using_name.sayHi();

from using_name import sayHi
sayHi();