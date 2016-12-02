#!/usr/bin/python

# try to occure an excepiton

import sys

try:
    s = raw_input('Enter somthing-->')
except EOFError:
    print('error of EOF!')
    sys.exit()
except:
    print('some other exception occurs!')

print('Done:')
