# -*- coding: utf-8 -*-

def readFile(name):
    f= None
    l = []
    try:
        f = open(name, 'r')
        while True:
            line = f.readline()
            if(len(line) == 0):
                break
            ts = line.split(',')
            for i in ts:
                l.append(int(i))

    except IOError as e:
        print("read file error %s"%e.message)
    finally:
        if(f is not None):
            f.close()

    return l

def Decode(L, Q):
    Len = len(L)
    for i in range(0, Len):
        L[i]   ^= Q[i%3]
        if L[i] < 32 or L[i] > 127:
            return 0

    Sum=0
    for i in L:
        Sum += i

    return Sum

def FindResult(L):
    W=[0,0,0]
    start = ord('a')
    end = start+26
    for i in range(start, end):
        W[0]=i
        for j in range(start, end):
            W[1]=j
            for k in range(start, end):
                W[2]=k
                rc = Decode(L, W)
                if rc != 0:
                    print(rc)
                    print("%d%d%d "%(W[0],W[1],W[2])),

    return 0


if __name__ == '__main__':
    L = readFile("cipher.txt")
    FindResult(L)
