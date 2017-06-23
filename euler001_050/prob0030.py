""" Solution to Project Euler #30
https://projecteuler.net
"""

def IsDigitFifthPower(N):
  if N == 1 or N==0: return False
  a = 0
  ntmp = N
  while ntmp >0:
    a += (ntmp%10)**5 
    ntmp = ntmp//10

  if N == a:
    print('%i is a digit fifth power'%(N,))
    return True

  return False

def SumOfPowers():

  values = range(2,1000000)
  sum = 0
  for a in values:
    if IsDigitFifthPower(a):
      sum+= a

  return sum

if __name__=='__main__':
  print('Sum of all 5th digit powers: %i'%(SumOfPowers()))
