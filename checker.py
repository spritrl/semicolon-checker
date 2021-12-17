#! usr/bin/python
# -*- coding: ISO-8859-1 -*-
# Spritrl - REALINI Christophe 17/12/2021 - FR

import sys

isPythonFile = False

if len(sys.argv) < 2:
    print('You need to put your file in argument.')
    sys.exit()

fileName = sys.argv[len(sys.argv)-1]

if fileName[-2:] == 'py':
    isPythonFile = True
    print('Are you serious ? You don\'t need semicolon in Python :)')

if isPythonFile == False:
    f = open(fileName, 'r')
    accepted = ['{', '}', ':', ';', '*', '/', '\n']
    line = 0
    fails = []
    for l in f:
        line += 1
        lineSize = len(l)
        if l[lineSize - 2] in accepted:
            continue
        else:
            isFailed = True
            for c in l:
                if c == '/':
                    isFailed = False
            if isFailed:
                fails.append(line)

    print('Are you serious ? YOUR \';\' !')
    for fail in fails:
        print('ERROR : line ', fail)
