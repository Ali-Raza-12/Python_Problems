# Reverse a Number in Python using While Loop
# Reverse a Number in Python using Slice Operator
# Reverse a Number in Python using Recursion

# =====================================================

# Method 1: Reverse a Number in Python using While Loop

# n = int(input('Enter numbers:'))
# while n > 0:
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n // 10
# print(rev)

# ========================================================

# Method 2: Reverse a Number in Python using Slice Operator

# n = int(input('Enter Numbers:'))
# rev = int(str(n)[::-1])
# print(rev)

# ==========================================================

# Method 3 Reverse a Number in Python using Recursion

def reverse_number(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_number = number // 10
        reversed_number = reverse_number(remaining_number)
        return int(str(last_digit) + str(reversed_number))
 
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)