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


if __name__ == '__main__':
    #i=7
    p1=3
    p2=5
    counter = 0
    for i in range(7, 100, 2):
        if isPrime(i):
            P = (p1**3)*(p2**2)
            #  if "200" in str(P):
            print(P)
            Q = (p1**2)*(p2**3)
            #  if "200" in str(Q):
            print(Q)
            p2 = i
            p1 = p2


