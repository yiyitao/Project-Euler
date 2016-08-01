#-*- coding: utf-8 -*-

if __name__ == '__main__':
    f1 = 1
    f2 = 1
    cnt = 3
    limit = 10**1000
    while True:
        fn = f1+f2
        if fn >= limit:
            print("answer is %d"%(cnt))
            break
        f1 = f2
        f2 = fn
        cnt = cnt+1