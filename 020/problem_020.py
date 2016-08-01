# -*- coding: utf-8 -*-

def Factorial(n):
    assert(n > 0)
    if n == 0:
        return 1
    product=1
    for i in range(1, n+1):
        product *= i
    return product


def CalcBitSum(n):
    Sum = 0
    N = n
    while True:
        Sum += N%10
        N /= 10
        if N == 0:
            break

    return Sum

if __name__ == '__main__':
    print(CalcBitSum(Factorial(100)))
