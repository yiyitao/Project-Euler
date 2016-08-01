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


def FindNthPrime(N):
    assert(N > 0)
    if N==1:
        return 2

    num=3
    i=1
    while True:
        if isPrime(num):
            i+=1
            if(i == N):
                return num
        num += 2


if __name__ == '__main__':
    print("result = %d"%FindNthPrime(10001))


