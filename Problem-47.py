# Python Program to Print an Identity Matrix

n = int(input('Enter a num:'))

for i in range(0, n):
    for j in range(0, n):
        if i==j:
            print('1', sep=' ', end=' ')
        else:
            print('0', sep=' ', end=' ')
    print()

