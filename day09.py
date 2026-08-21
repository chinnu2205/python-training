#LINK: https://www.hackerrank.com/challenges/py-if-else/problem
#Task:1
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
n = int(input(3))

if n % 2 == 1:
  print('Weird')
elif n % 2==0 and  2 <= n <= 5:
  print(' not Weird')
elif n % 2 ==0 and 6 <= n <= 20:
  print('Weird')
else:
  print('not Weird')
  
  
 # LINK: https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year) :
  if year % 400 == 0:
     return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else :
    return False


#take n, if n from 1 to 7 print dayname else print invalid day number
#e.g. 1 - Sunday, 2 - Monday, 3 - Tuesday
n = int(input('Enter the day number'))
match n:
    case 1: print('sunday')
    case 2: print('monday')
    case 3: print('tuesday')
    case 4: print('wednesday')
    case 5: print('thurseday')
    case 6: print('friday')
    case 7: print('saturday')