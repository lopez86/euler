""" Solution to Project Euler prob 7
https://projecteuler.net/
"""


#! /usr/bin/env python3
import sys

def PrimeCounter(x):
  if x < 1: return -1
  if x == 1: return 2
  n = 3
  primes = [2]
  while (len(primes)< x):
 
    if IsPrime(n,primes):
 #     print (n)   
 #     sys.stdout.flush()
      primes.append( n )
    n+= 2 # don't care about evens
    if n < primes[-1]:
      print('Integer Overflow') 
      return -1
  return primes[-1]
    
def IsPrime(n,primes):
  max_val = n
  for p in primes:
  
    if p > max_val: break
    if n % p == 0:
      return False
    max_val = n / p
   
  return True

def run(x):
  print( PrimeCounter(x) )

if __name__=='__main__':
  run(10001)
