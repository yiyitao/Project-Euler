# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 21:06:02 2014

@author: dell
"""

def week(year, month, day):
    y = year%100
    c = year//100

    m = month
    if(m == 1 or m == 2):
        m = m +12
        if(y == 0):
            y = 99
            c = c - 1
        else:
            y = y-1

    d = day
    w = (y + y//4 + c//4 -2*c + (26*(m+1))//10 + d-1)%7
    return w

s = week(2015, 1, 25)
print("%d" %  s)

def sumSun(m, n):
    sum = 0
    for i in range(m, n+1):
        for j in range(1, 13):
            if(week(i, j, 1) == 0):
                sum = sum+1
    return sum

print(sumSun(1901, 2000))
