""" Solution to Project Euler prob 6
https://projecteuler.net/
"""


#! /usr/bin/env python3

def SumSquareDifference(N):
  val = 0
  for i in range(1,N+1):
    val +=  i * (N * (N+1) - i * (i+1))

  print('The difference between the square of the sum and\n'
        'sum of squares of natural numbers between 1 and %i is %i' %(N,val))
  

if __name__=='__main__':
  SumSquareDifference(100)
