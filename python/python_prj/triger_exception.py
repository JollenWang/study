#!/usr/bin/python

# trigger exception

class ShowInputException(Exception):
        '''User defined exception class'''
        def __init__(self, len, atleast):
            Exception.__init__(self)
            self.len = len
            self.atleast = atleast

try:
    str = input('wait for input:')
    L = len(str)
    if L < 3:
        raise ShowInputException(L, 3)
except EOFError:
    print('error of EOF!')
except ShowInputException(L, 3):
    print('The input length is %d, excepting at least %d' %(str.len, str.atleast))
else:
    print('no exception was raised!')


