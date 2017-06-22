""" Solution to Project Euler prob 76
https://projecteuler.net/
"""


#! /usr/bin/env python3

def SummationCounter(N,sums=[[0],[0,1]]):
  tot = 0

  if len(sums) >= N+1:
    return sum(sums[N])-1,sums

  if N == 2:
    sums.append([0,1,1])
    return 1,sums

  for i in range(len(sums),N):
    toti,sumi = SummationCounter(i,sums)
    sums = sumi
    
  sumN = [0]+[sum(sums[N-i][:i+1]) for i in range(1,N)] + [1]
  sums.append(sumN)
  tot += sum(sumN)
  print(N,tot-1)
  #print(sums)
  return tot-1,sums

if __name__=='__main__':
  SummationCounter(100)
