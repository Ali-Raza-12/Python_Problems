# Python Program to Count the Number of Digits in a Number

nmb = int(input('Enter a number:'))
count = 0
while(nmb!=0):
    count += 1
    nmb //= 10

print(count)
