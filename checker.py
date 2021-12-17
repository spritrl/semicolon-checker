isPythonFile = False
fileName = 'script.js'

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
