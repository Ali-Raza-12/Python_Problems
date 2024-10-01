# Python Program to Compute a Polynomial Equation

import math

print('Enter the coefficient of the form ax^3 + bx^2 + cx + d')
lst = []
for i in range(4):
    a=int(input('Enter the coefficient value:'))
    lst.append(a)
x = int(input('Enter a value of x:'))
sum1=0
for i in range(3):
    sum1 += lst[i] * math.pow(x, 3-i)

sum1 += lst[3]
print("The value of the polynomial is:", sum1)
