""" Solution to Project Euler #27
https://projecteuler.net
"""

def GetListOfPrimes(Nmax):

  if Nmax<2: return []
  if Nmax==2: return [2]
  
  primes = [2]

  for i in range(3,Nmax+1):
    isPrime = True

    for p in primes:
      if i % p ==0:
        isPrime = False
        break   

    if isPrime is True:
      primes.append(i)

  return primes

def QuadraticPrimes(max_coeff):

# b must be prime
  primes = GetListOfPrimes(2*max_coeff+1)

  max_primes = 0
  coef_prod = 0
  for b in primes:
    if b > max_coeff:
      continue
    for p in primes:
      a = p - b - 1
      if abs(a) >= max_coeff:
        continue

      n = 2
  
      while( n*n + a*n + b in primes):
        n += 1

      if n > max_primes:
        max_primes = n
        coef_prod = a*b

  return coef_prod,max_primes

if __name__=='__main__':
  prod,max_p = QuadraticPrimes(1000)
  print('The max product of the coefficients is %i'%(prod))
  print('  for %i consecutive primes'%(max_p))
