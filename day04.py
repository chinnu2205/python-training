print(10 + 5 * 2)   
print(2 ** 3 ** 2)  
print(10 // 3)    
print(10 % 3)     
print(5 / 2)        
print([1,2,3] + [4,5,6])
print((1,2,3) + (4,5,6))
print([1,2,3] * 4)
print(*[1,2,43])
#arithmetic operators
#relational operators and logical operators
print(10 > 5 and 20 < 30)
print(10 > 20 and 5 < 10)
print(not 1 == 1)
print(1 < 2 < 3)
print(1 > 2 > 3)
print('abc' > 'def')
print([1,2,3] < [1,3,4])
#assignment and walrus operator:
print(a:=10)
if (n := 34) > 10:
   print(n)
#Identity and equality operators:
a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)
a = 'abc'
b = 'abc'
print(a==b)
print(a is b)
a = (1,2,3)
b = (1,2,3)
print(a == b)
print(a is b)
#Membership operator
a = [1,2,3,4,5]
print(6 in a)
print(6 not in a)
print('abc' in 'abcde')