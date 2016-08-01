# -*- coding: utf-8 -*-

def Fibnoacci(n):
    assert(n >= 0)
    if(n <= 2):
        return n

    sum=0
    _1=1
    _2=2
    for i in range(3, n+1):
        sum = _1+_2
        _1=_2
        _2=sum

    return sum


if __name__ == "__main__":

    sum=0
    tmp=0

    for i in range(2, 1000, 3):
        tmp = Fibnoacci(i)
        if(tmp >= 4000000):
            break
        sum += tmp

    print("result = %d"%sum)
