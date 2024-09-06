# Python Program to Check Whether a Given Number is Perfect Number

n = int(input('Enter a no:'))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i

if(sum == n):
    print('Perfect no.')
else:
    print('Not perfect no.')
    
