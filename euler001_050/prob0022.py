""" Solution to Project Euler #22

https://projecteuler.net
"""

def NameScore(fname='names.txt'):
  names = []
  with open(fname) as f:
    names = f.read()

  names = names.replace('"','')
  names = names.replace('\n','')
  names = names.split(',')
  names = sorted(names)
  print(names[0:5],names[-5:-1])
  letters = {}
  for idx,s in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    letters[s] = idx+1

  total_score = 0
  for idx,name in enumerate(names):
    score = 0
    for l in name:
      score+= letters[l]
    score = score * (idx+1)
    total_score += score
  return total_score

if __name__ == '__main__':
  print(NameScore())
