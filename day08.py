#write the outputs before executing
#TASK 1
n = 9
if n % 3 == 0:
    print('A')
print('Outside')
'''
Write Output:A,OUTSIDE

'''

#TASK 2:
n = 10
if n % 10 == 0:
    print('A')
if n % 5 == 0:
    print('B')
print('Outside')
'''
Write Output: A , B, OUTSIDE N CAN DIVISIBLE BY BOTH 10 AND 5 AND COME OUTSIDE

'''


#TASK 3:
n = 10 
if n % 10 == 0:
    print('A')
elif n % 5 == 0:
    print('B')
print('Outside')
'''
Write Output: A ,OUTSIDE BECAUSE THE  1ST IF CONDITION IS TRUE SO CURSOR COME OUT DOES NOT GO TO ELIF CONDITION

'''

#TASK 4:
n = 10 
if n % 6 == 0:
    print('A')
elif n % 3 == 0:
    print('B')
else:
    print('C')
print('Outside')
'''
Write Output: PRINTS C AND OUTSIDE, BECAUSE IST 2 IF STATEMENTS ARE FALSE 
SO CURSOR CHOOSES ELSE STATEMENT
'''

#TASK 5:
marks = 89 
if marks > 40:
    if marks > 75:
        print('Dictinction') 
    else:
        print('Pass')
else:
    print('Fail')
'''
Write Output: PRINT DICTINCTION BECAUSE THE GIVEN MARKS ARE GREATER THAN 75 SO SECOND IF STATEMENT
CORRECT SO CURSOR CHOOSES 2ND IF STATEMENT AND COMES OUTSIDE
'''