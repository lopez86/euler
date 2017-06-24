""" Solution to Project Euler #26
https://projecteuler.net
"""

def ReciprocalCycle(d):

  while d%2==0: d = d // 2
  while d%5==0: d = d // 5

  a = 1
  n = 9
  if d==1: return 0
  while( (n%d) != 0):
    a+=1
    n = n * 10 + 9
  return a

def FindLargest(nmax):

  amax = 0
  dmax = 0
  for d in range(2,nmax):
    a = ReciprocalCycle(d)
    if a > amax:
      dmax = d
      amax = a
      print('New max at %i length %i'%(dmax,amax))
  print(amax,dmax)


if __name__=='__main__':

  FindLargest(1000)
