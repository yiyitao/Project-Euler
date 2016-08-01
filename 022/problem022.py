# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 20:38:34 2014

@author: dell
"""

def readFile(name):
    f= None
    l = []
    try:
        f = open(name, 'r')
        while True:
            line = f.readline()
            if(len(line) == 0):
                break
            ts = line.split(',')
            for i in ts:
                l.append(i)

    except IOError as e:
        print("read file error %s"%e.message)
    finally:
        if(f is not None):
            f.close()

    return l

def wordScore(word):
    sum = 0
    for i in range(1, len(word)-1): #名字本身就含有引号
        sum  = sum + ord(word[i]) - ord('A')+1
    return sum

def calcSumScore(name):
    l = readFile(name)
    l.sort()
    sum = 0
    for i in range(0, len(l)):
        sum = sum + (i+1)*wordScore(l[i])
    return sum


#print(wordScore("COLIN")*938)
print(calcSumScore("names.txt"))
#l = readFile("names.txt")
#l.sort()
#print(wordScore(l[937]))
#print(type(l[937]), l[937])
#print(l[937])
#print(wordScore("\"COLIN\""))
