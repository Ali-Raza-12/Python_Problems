# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

min = int(input('Enter min range:'))
max = int(input('Enter max range:'))

for i in range(min, max):
    if( i%7==0 and i%5==0):
        print(i)