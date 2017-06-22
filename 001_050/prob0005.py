""" Solution to Project Euler prob 5
https://projecteuler.net/
"""


#! /usr/bin/env python3

def ListOfPrimes(nmax):
  primes = [2]
  x = 3
  while(x<=nmax):
    isPrime = True
    for p in primes:
      if x % p == 0:
        isPrime = False
        break
    if isPrime is True:
      primes.append(x)
    x += 2
  return primes
def SmallestMultiple(nmax):
  primes = ListOfPrimes(nmax)
  divisors = range(2,nmax+1)
  #print(primes)
  #print(divisors)
  prime_counts = dict((p,1) for p in primes )
  for d in divisors:
    for p in primes:
      if p>= d/2: break
      n = 0
      while d%p==0:
        n += 1
        d /= p
      
      prime_counts[p] = max(prime_counts[p],n)

  total = 1
  print(prime_counts)
  for key in prime_counts:
    total *= key**(prime_counts[key])
  print('Smallest multiple of integers is [1,%i] is %i'%(nmax,total))

if __name__=='__main__':
  SmallestMultiple(20)
  
  
