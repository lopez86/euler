""" Solution to Project Euler prob 15
https://projecteuler.net/
"""

from scipy.special import comb

def lattice_path(N):
  return comb(2*N,N,exact=True)


if __name__=='__main__':
  print(lattice_path(20))
