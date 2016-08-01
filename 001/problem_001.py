# -*- coding: utf-8 -*-

# answer is 233168

def sum1toN(n):
   return n * (n + 1) / 2

def sumMultiples(limit, a):
   return sum1toN((limit - 1) / a) * a

if __name__ == '__main__':
    N=1000
    result = sumMultiples(N, 3) + sumMultiples(N, 5) - sumMultiples(N, 15)
    print("result = %d"% result)
