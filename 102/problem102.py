# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 20:37:51 2014

@author: dell
"""

import math

#  import numpy as np

def readFile(name):
    f= None
    l = []
    try:
        f = open(name, 'r')
        while True:
            #  q = np.array([
            #  [0, 0],[0, 0],[0, 0]
            #  ])

            q = []

            line = f.readline()
            if(len(line) == 0):
                break
            ts = line.split(',')
            assert(len(ts) == 6)
            q.insert(0, (int(ts[0]),int(ts[1])))
            q.insert(1, (int(ts[2]),int(ts[3])))
            q.insert(2, (int(ts[4]),int(ts[5])))


            l.append(q)

    except IOError as e:
        print("read file error %s"%e.message)
    finally:
        if(f is not None):
            f.close()

    return l


def direction(Pi, Pj, Pk):
    p1=(Pk[0]-Pi[0], Pk[1]-Pi[1])
    p2=(Pj[0]-Pi[0], Pj[1]-Pi[1])

    return p1[0]*p2[1] - p1[1]*p2[0]

def isInner(a,b,c):
    o=(0,0)
    d1 = direction(o,a,b)
    d2 = direction(o,a,c)
    d3 = direction(o,c,b)
    d4 = direction(o,c,a)
    if d1*d2 <= 0 and d3*d4 <= 0:
        return True;
    return False

if __name__ == '__main__':
    fl = readFile("triangles.txt")
    Sum=0
    for p in fl:
        if(isInner(p[0], p[1], p[2])):
            Sum += 1

    print("result = %d"%Sum)


