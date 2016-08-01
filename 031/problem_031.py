# -*- coding: utf-8 -*-

#  coins=[1,2,5,10,20,50,100,200]
#  amount=200
#  #  memo[0..amount][2..8]={all0}
#  memo = [[0]*8 for i in xrange(200)]
#  def ways(target,avc):
#      if avc<=1:
#          return 1
#      t=target

#      if memo[t][avc]>0:
#          return memo[t][avc]

#      res=0
#      while target>=0:
#          res += ways(target,avc-1)
#          target = target - coins[avc]
#      memo[t][avc]=res

#      return res

#  print(ways(amount-1,7))

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
ways = [0 for i in xrange(200)]
ways[0] = 1
for i in xrange(0,8):
    for j in xrange(coins[i], amount):
        ways[j] = ways[j] + ways[j-coins[i]]

print(ways[amount-1])
