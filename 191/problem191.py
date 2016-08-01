# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 18:20:15 2014

@author: dell
"""



def fun(x):
    lst = [1, 3, 0, 2, 1, 0, 0, 1]

    while lst[0] < x:
        n, t, a, b, c, d, e, f = lst
        lst = [n + 1, 2 * t + b - a, c, 2 * b - a + d, t - (a + c), e, f, t]

    return lst[1]


for i in range(3, 31):
    print(str(i) + " : %d" % fun(i))


