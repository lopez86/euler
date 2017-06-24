""" Solution to Project Euler #39
https://projecteuler.net
"""

#squares = []

#def build_squares(Nmax):
#  global squares 
#  squares = [a*a for a in range(1,Nmax+1)]


def count_solutions(p):
  solutions = 0
  for a in reversed(range(1,p//2-1)):


    for b in reversed(range(1,a)):
      c = p - a - b
      if c>b: break
      if a*a -b*b-c*c==0:
        solutions+=1

  return solutions

def find_most_solutions(Nmax=1000):
#  build_squares(Nmax)
  max_solutions = 0
  nmax = 0
  for i in range(5,Nmax+1):
    sols = count_solutions(i)
    if sols >= max_solutions:
      print(i, sols)
      max_solutions = sols
      nmax = i

  return nmax

if __name__=='__main__':
  print(count_solutions(120))
  nmax = find_most_solutions()
  print("Triangle perimeter with most integer-sided right triangles: "+str(nmax))
