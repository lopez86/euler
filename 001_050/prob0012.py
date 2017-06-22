""" Solution to Project Euler prob 12
https://projecteuler.net/
"""


#! /usr/bin
from math import sqrt

def ListOfPrimes(nmax,primes=[2]):
  x = max(primes)+1
  while x<=nmax:
    isPrime = True
    for p in primes:
      if x % p == 0:
        isPrime = False
        break
    if isPrime is True:
      primes.append(x)
    x += 2
  return primes

def GetFactors(theNum,primes=[2]):
  
  num_tmp = theNum
  if theNum/2+1 > primes[-1]:
    primes = ListOfPrimes(sqrt(theNum),primes)
  nfact = 1
  for p in primes:
    n = 1
    if p > theNum: break
    while theNum % p == 0:
      theNum = theNum / p
      n += 1
    nfact *= n

  if nfact == 1:
    nfact = 2
  return nfact,primes

def TriangularDivisors(ndiv):

  # For speed
  primes = ListOfPrimes(13000)

  if ndiv == 1: return 1
  if ndiv ==2: return 3
  div = 0
  theNum = 3
  i = 2
#  theDict = {3}
  maxDiv = 2
  while div <= ndiv:
    i+=1
    theNum = i*(i+1)//2
    
    num_tmp = theNum
    if sqrt(theNum) > primes[-1]:
      primes = ListOfPrimes(sqrt(theNum),primes)
    div = 1
    for p in primes:
      n = 1
      if p > theNum: break
      while num_tmp % p == 0:
        num_tmp = num_tmp / p
        n += 1
      div *= n
  
    if div == 1:
      div = 2
#    if div > maxDiv:
#      print(i,theNum,div)
#      maxDiv = div
  return i*(i+1)//2



if __name__=='__main__':
  n = 500
  num = TriangularDivisors(n)

  print('%i is the first triangular number to have over %i divisors'%(num,n))
