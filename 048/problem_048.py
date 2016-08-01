# -*- coding: utf-8 -*-


import math

def Select(n,k):
    assert(n >= k)
    if(n == k or k == 0):
        return 1
    m=1
    for i in range(n, n-k, -1):
        m *= i

    return m/math.factorial(k)

if __name__ == '__main__':
    Sum = 0
    for i in range(0, 100):
        for j in range(0, 10):
            for k in range(0, 10*i+j+1):
                if k < 10:
                    Sum += Select(10*i+j, k)*((10*i)**k)*(j**(10*i+j-k))

    print(Sum%10000000000 - 1)

