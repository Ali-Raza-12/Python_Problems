# Python Program to Print the Fibonacci Sequence

def fibanacci(n):
    if n <= 1:
        return n
    else:
        return(fibanacci(n-1) + fibanacci(n-2))

n = int(input('Enter a numb:'))
print('Sequence of Fibonacci is :')

for i in range(n):
    print(fibanacci(i))