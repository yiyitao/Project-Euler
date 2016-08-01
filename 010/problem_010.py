# -*- coding: utf-8 -*-

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


def SummationOfPrimes(n):
    assert(n>=2)
    Sum=2
    for i in range(3,n,2):
        if(isPrime(i)):
            Sum += i

    return Sum


if __name__ == '__main__':
    print("result = %d"%SummationOfPrimes(2000000))
