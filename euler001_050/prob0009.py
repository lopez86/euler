""" Solution to Project Euler prob 9
https://projecteuler.net/
"""


#! /usr/bin/env python3
from math import *
# Find a Pythagorean triplet:
def PythagoreanTriplet(theSum):

  triplet = []

  squares = [x*x for x in range(1,theSum // 2 +1)]
  # probably a better # to use here
  # I think maybe sum / (1+sqrt(2)) + 1 is better
#  print(squares)
  N = len(squares)
  for i in range(0,N):
    sq1 = squares[-1-i]
    breakLoop = False
    for j in range(0,N-i):
      sq2 = squares[-1-i-j]
      if sq1-sq2 in squares:
        ii = N-i
        jj = N-i-j
        k = squares.index(sq1-sq2)+1
        if ii+jj+k == theSum:
          triplet = [k,jj,ii]
          breakLoop = True

    if breakLoop is True:
      break
  print('Triplet: ')
  print(triplet)
  print('Product: %i'%(triplet[0]*triplet[1]*triplet[2]))

if __name__=='__main__':
  PythagoreanTriplet(1000)
