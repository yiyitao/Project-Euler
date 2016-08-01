# -*- coding: utf-8 -*-


def TriangularNumber(n):
    return n*(n+1)/2

def DivisorsCount(n):
    Sum = 2
    s = (n/2)+1
    for i in range(2, n):
        if n%i == 0:
            Sum += 1

    return Sum

def HighlyDivisibleTriangularNumber(n):
    i=1
    while True:
        T = TriangularNumber(i)
        if DivisorsCount(T) >= n:
            return T
        i += 1

    return 0


if __name__ == '__main__':
    print("result = %d"%HighlyDivisibleTriangularNumber(200))
    #  for i in range(1,50):
    #      t = TriangularNumber(i)
    #      print("%d : %d      %d"%(i, t, DivisorsCount(t)))
