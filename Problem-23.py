# Python Program to Check Armstrong Number

n = int(input('Enter a no:'))
a = list(map(int, str(n)))
b = list(map(lambda x:x**3, a))

if sum(b) == n:
    print('Armstrong Number.')
else:
    print('Not a armstrong Number.')


