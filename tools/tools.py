""" Common tools for solving Euler problems"""


def GetListOfPrimes(Nmax,primes = [2],maxp=-1):

  if primes[-1]>=Nmax or maxp>Nmax:
    return primes
  if Nmax<2: return []
  if Nmax==2: return [2]

  maxval = max(primes[-1],maxp)

  for i in range(maxval,Nmax+1):
    isPrime = True

    for p in primes:
      if i % p ==0:
        isPrime = False
        break   

    if isPrime is True:
      primes.append(i)

  return primes

def GetPrimeDivisors(N,primes=[2],maxp=-1):
  primes = GetListOfPrimes(N,primes,maxp)
  if N in primes:
    return [N]

  divs = [] 
  Ntmp = N

  for p in primes:
    if p > Ntmp:
      break
    while Ntmp%p==0:
      divs.append(p)
      Ntmp = Ntmp/p

  return divs

def GetAllDivisors(N,primes=[2],maxp=-1):

  divs = GetPrimeDivisors(N,primes,maxp)

  ndivs = len(divs)
  nmax = 2**(len(divs) )
  all_divs = set()
  for i in range(nmax):
    n = 1
    for j in range(ndivs):
      bit = ((i>>j)&1)
      if bit==1:
        n*=divs[j]
    all_divs.add(n)
  return all_divs

