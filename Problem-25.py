# Python Program to Check if a Number is a Strong Number

sum = 0
num = int(input('Enter a number:'))
temp = num

while(num):
    r = num % 10
    i = 1
    f = 1

    while (i<=r):
        f = f*i
        i += 1
    sum = sum + f
    num = num // 10
    
if (sum == temp):
    print('Is Strong no.')
else:
    print('Not a Strong no.')