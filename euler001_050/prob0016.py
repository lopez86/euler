""" Solution to Project Euler prob 1
https://projecteuler.net/
"""

def PowerDigitSum(n):

  power = 2 ** n

  powerStr = str(power)
  return sum([int(x) for x in powerStr])


if __name__=='__main__':
  print(PowerDigitSum(1000))
