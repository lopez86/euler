""" Solution to Project Euler # 88
https://projecteuler.net
"""

import numpy as np
from functools import reduce

def GetPrimes(Nmax):
  if Nmax<=1: return []
  elif Nmax==2: return [2]
  
  primes = [2]
  for i in range(3,Nmax+1):
    isPrime = True
    for p in primes:
      if i%p == 0:
        isPrime = False

    if isPrime is True:
      primes.append(i)

  return primes

def GetPartitions(aList):

  if len(aList) == 0:
    yield []
    return
  if len(aList) == 1:
    yield [ aList ]
    return

  a = aList[0] # First element
  for b in GetPartitions(aList[1:]): # loop over subsets of remaining elements
    for idx,subset in enumerate(b):
      yield b[:idx] + [[a ] + subset] + b[idx+1:]
    yield [[ a ]] + b

def Factorize(N,primes):
  factors = []


  if N in primes:
    return []

  Ntmp = N
  for p in primes:
    while(Ntmp%p==0):
      factors.append(p)
      Ntmp = Ntmp//p


  prodsum = set()
  for part in GetPartitions(factors):
    theSum = sum([ reduce( (lambda x,y: x*y),p) for p in part])
    theLength = len(part) + (N-theSum) # fill with ones
    if theLength>1:
      prodsum.add(theLength)

  return prodsum# set of values for which this is a valid product-sum number

def ProductSumNumbers(N):
  primes = GetPrimes(2*N+1)# prob. don't need the +1
  
  prod_sum = np.zeros(N+1)

  for i in range(2,2*N+1):
    if i%1000==0: print(i)
    ps = Factorize(i,primes)
    for p in ps:
      if p<len(prod_sum) and prod_sum[p] == 0:
        prod_sum[p] = i
    if min(prod_sum[2:])>0:
      break

  #print(prod_sum)
  print("the sum of all the minimal product-sum numbers for 2 to %i"%(N))
  print("is %i"%(sum(set(prod_sum))))

if __name__ == '__main__':
  ProductSumNumbers(12000)
