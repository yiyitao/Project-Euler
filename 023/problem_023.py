# -*- coding: utf-8 -*-


def isAbundant(n):
    assert(n > 0)
    m = n/2 +1
    Sum = 0
    for i in range(1, m):
        if n%i == 0:
            Sum += i

    return Sum > n

# def NonAbundantSums():

if __name__ == '__main__':
    pass
