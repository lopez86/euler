""" Solution to Project Euler prob 4
https://projecteuler.net/
"""


#! /usr/bin/env python3

def Palindrome():

## 6 digit
  for i in reversed(range(1,10)):
    for j in reversed(range(10)):
      for k in reversed(range(10)):
        num = 100001 * i + 10010 * j + 1100*k

        good,ii,jj = Has3DigitFactors(num)

#        if num == 906609: print(num,i,j)
        if good: return num,ii,jj
        

## 5 digit
  for i in reversed(range(1,10)):
    for j in reversed(range(10)):
      for k in reversed(range(10)):
        num = 10001 * i + 1010 * j + 100*k
        good,i,j = Has3DigitFactors(num)
        if good: return num,i,j

  return -1

def Has3DigitFactors(num):
  maxval = 1000
  for i in range(100,1000):
### If it divides properly
    if i > maxval: break
    if num % i == 0:
      j = int(num / i)
      if 100 <= j < 1000: 
        return True, i,j
    maxval = num/i+1

  return False,-1,-1


def run():
  num0,i0,j0 = Palindrome()
  print (str(num0)+' = ' + str(i0) + ' x ' + str(j0))

if __name__=='__main__':
  run()
