# Method 1: Factorial in Python using While Loop (Without Recursion)

# n = int(input('Enter a number:'))

# fact = 1

# while(n > 0):
#     fact = fact * n
#     n = n - 1

# print('Factorial number is:', fact)

# ========================================================================

# Method 2: Factorial in Python using Recursion

def fact(n):
    if n <= 0:
        return 1
    else:
        return (n*fact(n-1))

n = int(input('Enter a number:'))
print('factorial of number is:')
print(fact(n))


# ===============================================================

# Method 3: Factorial in Python using Function

# import math

# def fact(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative number.")
#     else:
#         return math.factorial(n)
    
# n = int(input('Enter a number:'))
# factorial = fact(n)
# print('Factorial of {} is {}'.format(n, factorial))

