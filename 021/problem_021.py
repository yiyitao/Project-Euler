# -*- coding: utf-8 -*-

def ProperDivisorsSum(n):
    #  assert(n > 0)
    m = (n/2) +1
    Sum = 0
    for i in range(1, m):
        if n%i == 0:
            Sum += i
    return Sum


def AmicableNumbersSum(n):
    Sum = 0
    l=[]
    for i in range(1,n):
        if i in l:
            continue
        a = ProperDivisorsSum(i)
        b = ProperDivisorsSum(a)
        if i == b and b != a:
            Sum += i+a
            if a > b:
                l.append(a)

    return Sum



if __name__ == '__main__':
    print(AmicableNumbersSum(10000))
