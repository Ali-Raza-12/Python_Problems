# Python Program to Find the Sum of Natural Numbers

n = int(input('Enter a limit:'))

sum = 0
for i in range(1, n+1):
    sum += i

print('Sum of Natural number :', sum)