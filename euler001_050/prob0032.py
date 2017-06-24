""" Solution to Project Euler #32
https://projecteuler.net
"""

def PandigitalProducts():

  prodSet = set()
  for i in range(2,100):
    
    ndig = 1
    if i//10>0:
      ndig = 2
    if i//100>0:
      ndig=3

    for j in range( i+1,5000):

      ndig2 = 1
      if j//10>0:
        ndig2 = 2
      if j//100>0:
        ndig2=3
      if j//1000>0:
        ndig2=4

      if (i*j) >= 10**(9- ndig-ndig2):
        break
  
      digits = set([int(s) for s in str(i)] 
               + [int(s) for s in str(j)] 
               + [int(s) for s in str(i*j)] )

      if (len(digits)==9) and 0 not in digits:
        prodSet.add(i*j)

  return sum(prodSet)


if __name__=='__main__':
  print(PandigitalProducts())
