# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 10:01:49 2014

@author: dell
"""

def fibSum(n):
    l=[1,2]
    a=0
    b=0
    sum = l[1]
    i=0
    while True:
        a = l[i]
        b = l[i+1]
        l.append(a+b)
        if(l[i+2] > n):
            break
        if(l[i+2]%2 == 0):
            sum = sum + l[i+2]
        i = i+1
    return sum, i, l[len(l)-1]

s = fibSum(4000000)
print(s)
