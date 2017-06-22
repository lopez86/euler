""" Solution to Project Euler prob 17

https://projecteuler.net
"""

# Works at least up to 99999

ones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
def NumberLetterCounts(n):

  ones_place = n%10
  tens_place = (n//10) %10
  hds_place = (n//100) % 10
  th_place = (n//1000) %10
  tnth_place = (n//10000) %10
  
  length = 0
  if tens_place < 2:
    length += ones[tens_place*10+ones_place]
  else:
    length += ones[ones_place]
    length += tens[tens_place]

  

  if (hds_place!=0 or th_place!=0 or tnth_place!=0) and (tens_place>0 or ones_place>0):
    length += 3 #and
  if hds_place!=0:
    length += 7 # hundred
    length += ones[hds_place]
 
  if tnth_place!=0 or th_place!=0:
    if  tnth_place < 2:
      length += ones[tnth_place*10+th_place]
      length += 8 # thousand
    else:
      length += 8 #thousand
      length += ones[th_place]
      length += tens[tnth_place]
  
  return length
    

def SumUpNumbers(n):
  theSum = 0
  for i in range(1,n+1):
    theSum += NumberLetterCounts(i) 
  return theSum

if __name__=='__main__':
  print(SumUpNumbers(1000))
