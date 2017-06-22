""" Solution to Project Euler prob 93
https://projecteuler.net/
"""


#! /usr/bin/env python3

import operator
import itertools
def ListOfNums(x1,x2,x3,x4):

  ops = [operator.add, operator.sub, operator.mul, operator.truediv]

  theList = []
  for per in itertools.permutations([x1,x2,x3,x4]):
    a = per[0]
    b = per[1]
    c = per[2]
    d = per[3]

    for op1 in ops:
      for op2 in ops:
        for op3 in ops:
  
          try:
            x=op3(op2(op1(a,b),c),d) #a,b,c,d
            if x>0:
              theList.append(x)
          except:
            pass
          try:
            x=op3(op1(a,op2(b,c)),d ) #a,(b,c),d
            if x>0:
              theList.append(x)
          except:
            pass
          try:
            x=op2(op1(a,b),op3(c,d)) #(a,b)(c,d)=a,b(c,d)
            if x>0:
              theList.append(x)
          except:
            pass
          try:
            x=op1(a,op3(op2(b,c),d )) # a(b,c,d)
            if x>0:
              theList.append(x)
          except:
            pass
          try:
  
            x=op1(a,op2(b,op3(c,d) )) # a(b,(c,d))
            if x>0:
              theList.append(x)
          except:
            pass
        #  try:
        #    x=op3(op1(a,op2(b,c)),d) # ((a,(b,c)),d))
        #    if x>0:
        #      theList.append(x)
        #  except:
        #    pass
  
  theList = [int(x) for x in theList if int(x)==x ]
  aSet = sorted(set(theList))
  diffs = [aSet[i+1]-aSet[i] for i in range(len(aSet)-1)]

  cons = 1
  for i in range(len(diffs)):
    if diffs[i]!=1:
      cons = i+1
      break
#  print(len(aSet)) 
#  print(aSet)
  return cons,aSet

def LoopOverSets(nmax=9):

  maxCons = 1
  theList = [0,0,0,0]
  for x1 in range(1,nmax-2):
    for x2 in range(x1+1,nmax-1):
      for x3 in range(x2+1,nmax):
        for x4 in range(x3+1,nmax+1):
          ncons,aSet = ListOfNums(x1,x2,x3,x4)
          #print(ncons,[x1,x2,x3,x4])
          if ncons > maxCons:
            maxCons = ncons
            theList = [x1,x2,x3,x4]
            
  theList = [str(x) for x in theList]
  theString = ''.join(theList)
  print(theString)

if __name__=='__main__':
  LoopOverSets()
          
