#!/usr/bin/python

# python libs

import sys

#print(sys.version)
#print(sys.version_info)

def readfile(filename):
    '''print a file to the standard output'''
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
    f.close()

# script starts from here
if len(sys.argv) < 2:
    print("No action specified!")
    sys,exit()

if sys.argv[1].startswith("--"):
    option = sys.argv[1][2:]
    if option == "version":
        print("python version:1.2")
    elif option == "help":
        print(''' \
        This program prints files to the standard output.
        Any number of files can be specified.
        Options include:
        --help: Display this help
        --version: Prints the version number''')
    else:
        print('Unkonwn option')
    sys.exit()
else:
    for file in sys.argv[1:]:
        readfile(file)
