# Method 1: Palindrome Program in Python using While Loop

# n = int(input('Enter a number:'))
# temp = n
# rev = 0

# while n > 0:
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n // 10

# if (temp == rev):
#     print('N is palindrome')
# else:
#     print('N is not palindrom')

# =============================================================

# Method 2: Palindrome in Python using Built-in Function

# def palindrome(n):
#     return str(n) == ''.join(reversed(str(n)))
    
# n = int(input('Enter a string:'))

# if  palindrome(n):
#     print(f'{n} is palindrome')
# else:
#     print(f'{n} is not palindrome')

# =================================================================

# Method 3: Palindrome in Python using Recursion

# def recursion(n, temp, rev=0):
#     if n == 0:
#         if temp == rev:
#             return 'N is palindrome'
#         else:
#             return 'N is not palindrome'
#     else:
#         dig = n % 10
#         rev = rev * 10 + dig
#         n = n // 10

#         return recursion(n, temp, rev)
    
# n = int(input('Enter a number:'))
# result = recursion(n, n)
# print(result)

# ===================================================================

# Method 4: Palindrome in Python using Slicing

def plaindrome(n):
    temp = str(n)
    rev = temp[::-1]
    return rev == temp

n = int(input('Enter a number:'))

if plaindrome(n):
    print('N is palindrome')
else:
    print('N is not plaindrome')