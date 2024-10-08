# Python Program to Swap Two Numbers without using Third Variable

a = int(input('Enter a value of a:'))
b = int(input('Enter a value of b:'))

c = a + b

a = c - a
b = c - b

print('Value of a after swaping:',a)
print('Value of b after swaping:',b)