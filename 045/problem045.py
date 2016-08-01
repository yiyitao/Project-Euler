# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 11:25:51 2014

@author: dell
"""

import math

def T(n):
    return n*(n+1)/2

def P(n):
    return n*(3*n-1)/2

def H(n):
    return n*(2*n - 1)

def TxIsInt(N):
    r = math.sqrt(1+8*N)

    if r != int(r):
        return False

    if (int(r)-1)%2 != 0:
        return False

    return True

def PxIsInt(N):
    r = math.sqrt(24*N+1)

    if r != int(r):
        return False

    if (int(r)+1)%6 != 0:
        return False

    return True

def HxIsInt(N):
    r = math.sqrt(8*N+1)

    if r != int(r):
        return False

    if (int(r)+1)%4 != 0:
        return False

    return True

def TPH(m):
    n = m
    while True:
        z = T(n)
        n += 1
        if(TxIsInt(z) and PxIsInt(z) and HxIsInt(z)):
            break

    return z

#n = T(286) - T(285)
#print(T(1))

if __name__ == '__main__':
    print("result = ",TPH(286))

