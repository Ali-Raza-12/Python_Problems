# Python Program to Find the Smallest Divisor of an Integer

n = int(input('Enter a number:'))
l = []
for i in range(2,n+1):
    if (n % i == 0):
        l.append(i)

print("Smallest divisor is:",l[0])