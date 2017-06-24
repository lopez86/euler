""" Solution to Project Euler #38
https://projecteuler.net
"""
import itertools
def pandigital_numbers():
  
  #List of pandigital numbers as strings
  pandigital = sorted( [ ''.join([str(b) for b in a]) for a in
                               itertools.permutations(range(1,10))],
                               reverse=True) 

  highest_pd = 0
  for idx,pd in enumerate(pandigital):
    if idx%10000==0: print('Entry: '+str(idx))
    for ndig in range(1,5):
      numstr = pd[0:ndig]
      num = int(numstr)
      i = 1
      while True:
        tmp =str( num * (i+1) )
        i+=1
        if len(numstr)+len(tmp) < 9:
          numstr = numstr + tmp
        elif len(numstr)+len(tmp)==9:
          numstr = numstr+tmp
          break
        else:
          break

      if numstr==pd:
        highest_pd = pd
        break
    if highest_pd!=0:
      break;
    
  return highest_pd


if __name__=='__main__':

  hpd = pandigital_numbers()
  print("Highest pandigital # that is the concatenated sum of "
        "(1,2,...) with some integer is "+str(hpd))
