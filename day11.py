#important problems
#1. print numbers from 1 to 10 
#for x in range(1,11):
    #print(x,end='')

#2. print even numbers from 5 to 30 and above list
#for x in range(1,31):
    #if x % 2 == 0:
      #print(x,end='')
    
#3. print odd numbers from 5 to 30 and above list
#for x in range(1,31):
    #if x % 2 == 1:
        #print(x,end='')

#4. print numbers divisible by 5 from 1 to 30 and above list
#for x in range(1,31):
    #if x % 5 == 0:
        #print (x,end=',')

#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list

#for x in range(1,101):
    #if x % 5 == 0 and x % 7 == 0 :
      #  print (x,end=',') # print(/n/n)/n means new line how many time we uses /n takes space
      
# f ''
#x = 50
#name = 'sumi'
#print (f'my name is {name},my marks are {x}')

#6. sum of numbers from 10 to 25 and above list
#sum = 0
#for x in range (10,26):
    #sum+=x
    #print('sum of numbers from 10 to 25 is :',sum)
    


#7. multiplication table of a number 
#n = int (input('ENTER A NUMBER FOR MULTIPLICATION:'))
#for i in range (1,11):
    #print(f'{n} * {i} = {n * i}')
#print()



#8. factorial 
# means multiplies the number given amd up to the number
# example
# given 5 factorial means 1*2*3*4*5 = 120
#n = int (input('enter a number for factorial : '))
#product = 1
#for x in range (1,n+1):
   # product *= x
#print (f'factorial of {n} is {product}')



#9. fibonacci 
# 1st term 0
#2nd term 1
#next terms sum of previous 2 terms
#ex 0 1 2 3 5 8 13 21
#n = int (input('enter a number for fibonacci terms :'))
#a = 0
#b = 1
#for x in range (n):
 # print(a,end='')
 #a , b = b , a+b
#print()

#10. reverse a string #
# this is solved by slicing same like range but creates new list
# (st end step ) ex list = [4,2,3,1,7,8] used in orderded sequences
#eg list,tuple,str,range ,bytes,bytearray
# syntax = sequence[star:end:step] 
#string = input ('enter a string')
#rev = ('')
#for x in range ( len(string)-1,-1,-1):
  #  rev += string[x]
#print (f'reverse of {string} is {rev}')




#11. count vowels in a string
string = input("enter a string:")

vowels = "aeiouAEIOU"
count = 0

for x in string:
    if x in vowels:
        count += 1
        
print("number of vowels: ",count)

#12. count z's and y's in a string
s = input("enter a string:")
count = 0
for x in s:
    if x in 'zZyY':
        count += 1
print(" Total z/'s and y/'s in given string",count )


#13. check whether a number is prime number or not
n = int(input('enter a number: ')) 
count = 0
if n < 2 :
    print('not prime')
else:
    for x in range (2,n):
       if n % x == 0:
           print('not prime')
           break
    else:
        print('prime')
    
    
     


