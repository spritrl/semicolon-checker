f = open("script.js", "r")

pythonFile = False
accepted = ['{', '}', ':', ';', '*', '/', '\n']
line = 0
fails = []

if pythonFile == False:
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
