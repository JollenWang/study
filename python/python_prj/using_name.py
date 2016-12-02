#!/usr/bin/python

#demo of using name in other modules

def sayHi():
    if __name__ == '__main__':
        print('This program is being run by itself');
    else:
        print('This program is being imported from another module');