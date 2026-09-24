# DAY 11: for loop
#important problems
#1. print numbers from 1 to 10 
for x in range(1, 11):
    print(x, end=' ')
print('\n')

list = [4,3,5,2,5,2,9,1,7,4,6,8]
#2. print even numbers from 5 to 30 and above list
for x in range(5, 31):  
    if x % 2 == 0:
        print(x, end=' ')
print()
for x in list:
    if x % 2 == 0:
        print(x, end=' ')
print('\n')

#3. print odd numbers from 5 to 30 and above list
for x in range(5, 31):
    if x % 2 == 1:
        print(x, end=' ')
print()
for x in list:
    if x % 2 == 1:
        print(x, end=' ')
print('\n')

#4. print numbers divisible by 5 from 1 to 30 and above list
for x in range(1, 31):
    if x % 5 == 0:
        print(x, end=' ')
print()
for x in list:
    if x % 5 == 0:
        print(x, end=' ')
print('\n')
#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
for x in range(1, 101):
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')
print()
for x in list:
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')
print('\n')

#6. sum of numbers from 10 to 25 and above list
sum = 0
for x in range(10, 26):
    sum += x
print('Sum of numbers from 10 to 25 is: ', sum)
print()
sum = 0
for x in list:  
    sum += x 
print('Sum of numbers in given list is, ', sum)

#7. multiplication table of a number 
n = int(input('Enter a number for multiplication:  '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
print()
#8. factorial 
n = int(input('Enter a number for factorial:  '))
product = 1 
for x in range(1, n + 1):
    product *= x 
print(f'Factorial of {n} is {product}')
#9. fibonacci 
n = int(input('Enter number of fibonacci terms:  '))
a = 0
b = 1
for x in range(n):
    print(a, end=' ')
    a, b = b, a+b 
print()
#10. reverse a string
string = input('Enter a string:  ')
rev = ''
for x in range(len(string)-1, -1, -1):
    rev += string[x]
print(f'Reverse of {string} is {rev}')

#11. count vowels in a string
s = input('Enter the string to count vowels:  ')
count = 0
for c in s:
    if c in 'aeiouAEIOU':
        count += 1 
print(f'Total vowels in the string is {count}')
#12. count z's and y's in a string
s = input('Enter the string to count z\'s and y\'s: ')
count = 0
for c in s:
    if c in 'zZyY':
        count += 1
print('Total z\'s and y\'s in given string is', count  )

#13. check whether a number is prime number or not 
n = int(input('Enter a number to check prime:  '))
if n < 2:
    print('Not Prime')
else:
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            print('Not Prime')
            break
    else:
        print('Prime')

#remove duplicates in list and in string
l = [1,2,2,2,3,4,5,6,5,6,7]
ul = [] 
for x in l:
    if x not in ul:
        ul.append(x)
print(ul)
s = 'rrraaaakkkkkeeeesssshhhh'
us = ''
for x in s:
    if x not in us:
        us += x 
print(us)










#DAY13 : while loop
#while loop
n = 5 
#infinite loop : runs infinitely without end
# while n >= 0:      
#     print('Hi')
#     print('Bye') 
# print('Outside')

n = 5 
while n >= 0:
    print(n, end=' ')
    n -= 1 
print('Outside')

n = 5 
while n <= 10:
    print(n, end=' ')
    n += 1 
print('Outside')

n = 5
while n <= 10:
    if n == 7:
        n += 1
        continue 
    print(n, end=' ')
    n += 1
else:
    print('Loop Successful')

n = 5
while n >= 0:
    if n == 3:
        break 
    print(n, end=' ')
    n -= 1
else:
    print('Loop Successful')
print()

#print 1 to 10 with while loop
n = 1 
while n <= 10:
    print(n, end=' ')
    n += 1 
print()
#print even numbers from 1 to 10
n = 2
while n <= 10:
    print(n, end=' ')
    n += 2
print()
#print numbers divisible by both 5 and 7 from 1 to 500 
n = 1 
while n <= 500:
    if n % 5 == 0 and n % 7 == 0:
        print(n, end=' ')
    n += 1 
print()

#count digits
n = int(input('Enter the number to count digits:  '))
count = 0
while n > 0:
    n = n // 10 
    count += 1
print(f'Number of digits in the given number is: {count}')

#reverse a number
n = int(input('Enter number to reverse:  '))
temp = abs(n)
rev = 0
while temp > 0:
    last_digit = temp % 10 
    rev = rev*10 + last_digit 
    temp //= 10 
if n < 0:
    rev = -rev 
print(f'Reverse of the given number is {rev}')

#palindrome number 
n = int(input('Enter a number to check palindrome:  '))
temp = abs(n)
rev = 0
while temp > 0:
    last_digit = temp % 10 
    rev = rev*10 + last_digit 
    temp //= 10 
if n < 0:
    rev = -rev 
if rev == n:
    print('Palindrome')
else:
    print('Not a Palindrome')

#armstrong number
n = int(input('Enter a number to check armstrong number:  '))
total_digits = len(str(n)) 
sum = 0 
temp = n 
while temp > 0:
    last_digit = temp % 10 
    sum += last_digit ** total_digits 
    temp //= 10 
if n == sum:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')

#palindrome string wihout slicing, without built in function
s = input('Enter a string to check palindrome:  ')
# method1 = reverse and check
# rev = ''
# for x in range(len(s)-1, -1, -1):
#     rev += s[x]
# if s == rev:
#     print('Palindrome')
# else:
#     print('Not a Palindrome')
# method2 = two pointers
i, j = 0, len(s)-1 
while i <= j:
    if s[i] != s[j]:
        print('Not a palindrome')
        break 
    i += 1 
    j -= 1 
else:
    print('Palindrome')










#DAY14: Nested loop and matrix
matrix = [ [4,5,6], [1,2,3], [7,8,9] ]
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c], end=' ')
    print()
print()
#colwise: it should be sqare matrix
for c in range(len(matrix[0])):
    for r in range(len(matrix)):
        print(matrix[r][c], end=' ')
    print()






#DAY15 Patterns
#right angle triangle
# n = int(input('Enter any integer number:  '))
n = 4
for i in range(1, n+1):
    print(i * '*')
print()
#inverted right angle triangle
for i in range(n, 0, -1):
    print(i * '*')
print()
#pyramid
for i in range(1, n+1):
    print( (n-i)*' ' + i*'* ' )
#inverted pyramid
for i in range(n, 0, -1):
    print( (n-i)*' ' + i*'* ' )
print()
#hollow sqare
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*', end='')
        else:
            print(' ', end='')
    print()
#star (zero based indexing)
for i in range(n):
    for j in range(n):
        if i == n//2 or j == n//2 or i == j or j == n-i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print() 

#NUMBER PATTERNS
#number right angle
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
#number inverted right angle
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
#same row pattern
for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
    print()
print()
#inverted same row pattern
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()
print()
#1's  pattern
for i in range(1, n+1):
    for j in range(i):
        print(1, end=' ')
    print()
print()
#inverted 1's  pattern
for i in range(n, 0, -1):
    for j in range(i):
        print(1, end=' ')
    print()
print()
#reverse number pattern
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()
#number pyramid
for i in range(1, n+1):
    print((n-i)*' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
#reverse number pyramid
for i in range(n, 0, -1):
    print((n-i)*' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
#pascal's triangle
for i in range(n):
    num = 1 
    for j in range(i+1):
        print(num, end=' ')
        num = num * (i-j) // (j+1)
    print()