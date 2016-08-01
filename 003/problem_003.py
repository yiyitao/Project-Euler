# -*- coding: utf-8 -*-

import math
def isPrime(n):
    s = int(math.sqrt(n))

    for i in range(s, 1, -1):
        if n%i == 0:
            return False
    return True

def MaxPrimeFactor(n):
    s = int(math.sqrt(n))

    for i in range(s, 1, -1):
        if n%i == 0 and isPrime(i):
            return i
    return 1


if __name__ == '__main__':

    print("result = %d"%MaxPrimeFactor(600851475143))
