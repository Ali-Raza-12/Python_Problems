# Python Program to Check Prime Number

a = int(input('Enter a number:'))
count = 0
for i in range(2, int(a**0.5) + 1):
    if a%i==0:
        count += 1
if(count<=0):
    print('Is a prime number')
else:
    print('Not a prime number')