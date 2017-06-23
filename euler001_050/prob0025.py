""" Solution to Project Euler #25
https://projecteuler.net
"""

def fibonacci_count(Ndigit):

  if Ndigit == 1: return 1

  f1 = 1
  f2 = 1
  i = 2
  while len(str(f2))<Ndigit:
    i += 1
    f1,f2 = f2,f1+f2

  return i

if __name__=='__main__':
  print(fibonacci_count(1000))
