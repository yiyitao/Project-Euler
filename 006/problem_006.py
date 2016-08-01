# -*- coding: utf-8 -*-


def SumofN(n):
    return n*(n+1)/2

def SumofSquare(n):
    return n*(n+1)*(2*n+1)/6

def SumSquareDifference(n):
    a = SumofN(n)
    b = SumofSquare(n)
    return a*a-b



if __name__ == '__main__':
    print("result : ", SumSquareDifference(100))

