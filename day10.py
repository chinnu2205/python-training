l = [4, 3, 2, 5, 6]
#print elements in list with for each loop
for x in (l):
   print(x , end = (''))
print()        #end works as space blt element 
   # not only space we can end by giving anyting 

#print elements in list with index based for loop
for x in range(len(l)): #0,1,2,3
   print(x,end='')
#skip printing even numbers in list
for x in l :
    if x % 2 == 0:
       continue
    print(x,end='')
print()
       

#skip printing odd numbers in list
for x in l:
   if x % 2 == 1:
      continue
   print(x,end='')
print()
#when number 2 comes stop printing  
for x in l :
    if x == 2 :
       break
    print(x,end='')
#when first odd number comes stop printing
if x in l :
   if x == 1:
      'break'
   print(x,end='')
   

#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for x in range(1,11) :
   print(x)
else:
   print('all numbers are printed')
print()
print()

   
   
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for x in range (1,11):
   if x % 2 == 0:
      continue
   print(x)
else:
   print('all numbers are printed')
print()
   
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for x in range (10,0,-1):
   if x == 5 :
      'break'
   print(x)
else:
   print('all numbers are printed')