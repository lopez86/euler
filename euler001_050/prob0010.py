""" Solution to Project Euler prob 10
https://projecteuler.net/
"""


#! /usr/bin/env python3 

from math import sqrt

def ListOfPrimes(nmax):
  primes = [2]
  x = 3
  while(x<=nmax):
    isPrime = True
    for p in primes:
      if p > sqrt(nmax): break
      if x % p == 0:
        isPrime = False
        break
    if isPrime is True:
      primes.append(x)
    x += 2

  return primes

def SumOfPrimes(nmax):
  primes= ListOfPrimes(nmax-1)
  prime_sum = sum(primes)
  print('Sum of primes below %i is %i'%(nmax,prime_sum))

if __name__=='__main__':
  SumOfPrimes(2000000)
