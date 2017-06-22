""" Solution to Project Euler prob 1
https://projecteuler.net/
"""

#! /usr/bin/env python3


## Sum of all multiples of n and m less than N

## Note: Sum(n in [1,N]) = 1/2 * N * (N+1)
def MultipleSum(n,m,N):
  nmax = N // n
  if N % n == 0: nmax -= 1
  mmax = N // m
  if N % m == 0: mmax -= 1

  nmmax = N // (n*m)
  if N % (n*m) == 0: nmmax -= 1

  return (n*nmax*(nmax+1) + m*mmax * (mmax+1) - n*m*nmmax*(nmmax+1) ) // 2


def run():
  print(MultipleSum(3,5,1000))

if __name__=='__main__':
  run()
