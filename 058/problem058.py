# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 19:46:49 2014

@author: dell
"""

#  import numpy as np


def getList(m):
    if m%2 == 0:
        raise "m must be odd"
    n = 2*m-1
    #  l = np.ndarray(n)
    l = [i for i in range(0,n)]
    l[0] = 1
    for i in range(1, n):
        l[i] = l[i-1] + ((i-1)//4 + 1)*2

    return l


def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2

    return True


def getPercent(l):
    cnt = 0
    for i in l:
        if(isPrime(i)):
            cnt += 1
    return cnt, l[len(l)-1], len(l),  cnt*1.0/len(l)

def getNextPercent(count, last, total, percent):
    #  l = np.ndarray(5)
    l = [i for i in range(0,5)]
    l[0] = last
    for i in range(1, 5):
        l[i] = l[i-1] + ((total-1)//4 + 1)*2
        total += 1
        if(isPrime(l[i])):
            count += 1

    return count, l[4], total, count*1.0/total

if __name__ == '__main__':
    q = getList(999)
    #  print(q)
    c, l, t, p = getPercent(q)
    #  print(c, l, t, p)

    while True:
        c, l, t, p = getNextPercent(c, l, t, p)
        #  print(c, l, t, p)
        if p < 0.10:
            print("the first less 10%% side length is %d" % ((t+1)/2))
            break;
