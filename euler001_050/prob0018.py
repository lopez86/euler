""" Solution to Project Euler problem #18
https://projecteuler.net
"""

def ReadFile(fname):

  nums=[]
  with open(fname) as f:
    lines = f.readlines()
    nums = [ [int(a) for a in line.split()] for line in lines]
  return nums

def TraverseGraph(nums):

  for i in range(1,len(nums)):
    for j in range(i+1):
      if j==0:
        nums[i][0] += nums[i-1][0]
      elif j==i:
        nums[i][i] += nums[i-1][i-1]
      else:
        n1 = nums[i-1][j-1]
        n2 = nums[i-1][j]
        nums[i][j] += max(n1,n2)
    print(nums[i])
  return max(nums[-1])

if __name__=='__main__':
  graph = ReadFile('prob0018.txt')
  print(TraverseGraph(graph))
