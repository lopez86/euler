""" Solution to Project Euler # 19
https://projecteuler.net
"""

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def SundayCount(ymin,ymax,start_day=1,ystart=1900):
  count = 0
  day_of_week = start_day
  for year in range(ystart,ymax+1):
    for month in range(12):

      if day_of_week==0 and year>=ymin: 
        count += 1
        print(year,month,day_of_week)   
      days = days_in_month[month]
      if (month==1) and \
         (year%4==0) and \
         (year%100!=0 or year%400==0):
        days+=1
      day_of_week = (day_of_week+days)%7

  return count

if __name__=='__main__':
#Sundays in January between 1901 and 2000, Jan 1 1901 is a Monday
  print(SundayCount(1901,2000,1,1900)) 
