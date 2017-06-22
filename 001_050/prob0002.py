""" Solution to Project Euler prob 2
https://projecteuler.net/
"""


#! /usr/bin/env python3

def FibonacciSequence(Nmax):
  if Nmax < 1: return []
  fib = [1,1]
  while fib[-1] < Nmax:
    next_val = fib[-1] + fib[-2]
    if next_val > Nmax: break
    fib.append(next_val)

  return fib

def EvenSum(Nmax):
  fib = FibonacciSequence(Nmax)
  total = 0
  for f in fib:
    if f % 2 == 0:
      total += f

  return total


def run():
  print(EvenSum(4000000))

if __name__=='__main__':
  run()
