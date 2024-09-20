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



# ========================================

# Fibonacci Series in Python using While Loop

# a=int(input("Enter the first number of the series "))
# b=int(input("Enter the second number of the series "))
# n=int(input("Enter the number of terms needed "))

# print(a, b, end=' ')

# while(n-2):
#     c = a + b
#     a = b
#     b = c
#     print(c, end=' ')
#     n -= 1

