# -*- coding: utf-8 -*-



if __name__ == '__main__':
    #  L=[i for i in range(0,10)]
    #  for i in L:
    #      print("%d"%i),

    M = [0,0,0,0]

    for i in range(0,24):
        M[i%4] = i%4
        print(M)

