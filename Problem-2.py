# Python Program to Print All Odd Numbers in a Range

lower = int(input('Enter lower range:'))
upper = int(input('Enter upper range:'))

for i in range(lower, upper):
    if i % 2 != 0:
        print(i)