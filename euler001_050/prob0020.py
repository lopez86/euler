""" Solution to Project Euler problem 20
https://projecteuler.net/problem=20
"""

from scipy.special import factorial

if __name__=='__main__':
  n = str(factorial(100,exact=True))
  print(sum([int(d) for d in n]))


