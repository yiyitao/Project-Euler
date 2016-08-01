# -*- coding: utf-8 -*-


def Factorial(n, m):
    assert(n >= m)
    result=1
    for i in range(0, m):
        result *= (n-i)

    return result


def GetSteps(n,m):
    return (Factorial(n+m,n))/Factorial(m,m)


if __name__ == '__main__':
    print(GetSteps(20,20))
