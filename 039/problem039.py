# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 11:53:31 2014

@author: dell
"""

def squareList(N):
    a = 3
    b = 4
    c = 5
    rl = []

    for i in range(3, N//3):
        a = i
        for j in range(N//3, N//2):
            b = j
            c = N-(a+b)
            l = []
            if a**2 + b**2 == c**2:
                l.append(a)
                l.append(b)
                l.append(c)
                rl.append(l)
                break

    return rl

if __name__ == '__main__':
    Max=0
    Len=0
    for i in range(12, 1001):
        Q = squareList(i)
        length = len(Q)
        if length > Len:
            Len = length
            Max = i
        #  print(i, ":", len(l))

    print("result = %d"%Max)

