# -*- coding: utf-8 -*-

def readFile(name):
    f= None
    M=[]
    try:
        f = open(name, 'r')
        while True:
            line = f.readline()
            if(len(line) == 0):
                break
            s = []
            if "Grid" in line:
                for i in xrange(0,9):
                    data = f.readline()
                    t=[k for k in xrange(0, 9)]
                    for j in xrange(0, 9):
                        t[j] = int(data[j])
                    s.append(t)
            M.append(s)

    except IOError as e:
        print("read file error %s"%e.message)
    finally:
        if(f is not None):
            f.close()

    return M

M = readFile("sudoku.txt")
for m in M:
    for mm in m:
        print(mm)
    print("==========================================")
