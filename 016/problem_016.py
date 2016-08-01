# -*- coding: utf-8 -*-


def PowerDigitSum(n):
    assert(n >= 0)
    num = 2**n
    Sum=0
    while True:
        Sum += num%10
        num /= 10
        if num == 0:
            break

    return Sum

if __name__ == '__main__':
    print(PowerDigitSum(1000))
