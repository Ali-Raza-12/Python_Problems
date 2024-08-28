# Using modulus operator


# n = int(input('Enter a number:'))
# if n % 2 == 0:
#     print(f'{n} is Ever')
# else:
#     print(f'{n} is Odd')

# ===========================================

# Using Bitwise operator


# n = int(input('Enter a number:'))
# if n & 1:
#     print(f'{n} is odd')
# else:
#     print(f'{n} is even')

# ==============================================

# # using Recursion

# n = int(input('Enter a number:'))

# def check(n):
#     if n < 2:
#         return( n % 2 == 0 )
#     return(check(n-2))

# if check(n) == True:
#     print(f'{n} is Even')
# else:
#     print(f'{n} is Odd')


# ================================================

# Using lambda function

check = lambda num: 'even' if num % 2 == 0 else 'odd'

num = int(input('Enter a number:'))

x = check(num)

print(x)