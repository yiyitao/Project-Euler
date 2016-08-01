# -*- coding: utf-8 -*-

import math

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


def GetPrimeFactor(n):
    l=[]
    for i in range(2,n+1):
        if(isPrime(i)):
            l.append(i)

    return l


def GetPrimeFactorMinMultipe(n):
    l = GetPrimeFactor(n)
    Q={}
    for e in l:
        f = 1
        if(e <= math.sqrt(n)):
            f = int(math.log(n, e))
        Q[e]=f

    result = 1
    for i in Q:
        result *= math.pow(i, Q[i])

    return result

if __name__ == '__main__':
    print("result : %d"%int(GetPrimeFactorMinMultipe(20)))


