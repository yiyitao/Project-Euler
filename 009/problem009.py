# -*- coding: utf-8 -*-


def PythagoreanTriplet(N):
    a = 0
    b = 0
    c = 0
    for i in range(3, N//3):
        a = i
        for j in range(i+1, N//2):
            b = j
            c = N-(a+b)
            if(a**2 + b**2 == c**2):
                return a,b,c

    return 0, 0, 0

a, b, c = PythagoreanTriplet(1000)
print(a, b, c)
print(a*b*c)
