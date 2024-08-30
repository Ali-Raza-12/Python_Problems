# Python Program to Print All Numbers in a Range Divisible by a Given Number

min = int(input('Enter min:'))
max = int(input('Enter max:'))

n = int(input('Enter Div:'))

for i in range(min, max):
    if(i%n==0):
        print(i)