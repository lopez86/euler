""" Solution to Project Euler prob 3
https://projecteuler.net/
"""


#! /usr/bin python3
import math

def PrimeSequence(Nmax):
  if Nmax < 2: return -1
  n = 3
  primes = [2]
  while primes[-1]< Nmax:

    if IsPrime(n,primes):
 #     print (n)   
 #     sys.stdout.flush()
      primes.append( n )
    n+= 2 # don't care about evens
    if n < primes[-1]:
      print('Integer Overflow')
      return -1
  return primes

def IsPrime(n,primes):
  max_val = n
  for p in primes:

    if p > max_val: break
    if n % p == 0:
      return False
    max_val = n / p

  return True

def LargestFactor(n):

  nmax = int(math.sqrt(n))+1
  primes = PrimeSequence(nmax)

  for prime in reversed(primes):
    if n % prime == 0:
      return prime

  # The number is prime, so return itself
  return n

def run():
  print(LargestFactor(600851475143))

if __name__=='__main__':
  run()
