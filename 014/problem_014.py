# -*- coding: utf-8 -*-

def StepNumber(n):
    step=0
    N=n
    while True:
        step += 1
        if N%2 == 0:
            N = N/2
        else:
            N = 3*N+1

        if N == 1:
            break

    return step


def FindMaxStep(n):
    Max = 0
    result = 0
    for i in range(2, n):
        step = StepNumber(i)
        if step > Max:
            Max = step
            result = i
    return result

if __name__ == '__main__':
    print("result = %d"%FindMaxStep(1000000))
