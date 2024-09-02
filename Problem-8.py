# Sum of Digits Program in Python

# Method-1
# n = input('Enter a num:')
# tot = 0 
# for i in str(n):
#     tot += int(i)
# print(tot)


# ========================================

# Method-2 using Function
# def sum(n):
#     tot = 0
#     for i in str(n):
#         tot += int(i)
#     return tot
    
# n = input('Enter a num:')
# Result = sum(n)
# print(Result)

# =============================================

# Method-3 Using Recursion

# l = []
# def sum(n):
#     if(n==0):
#         return l
#     first = n % 10
#     l.append(first)
#     sum(n // 10)

# n = int(input('Enter a num:'))
# print(sum(n))

# ==========================================================

# Method-4 Without Recursion in Python

l = []
b = int(input('Enter a number:'))
while(b>0):
    dig = b % 10
    l.append(dig)
    b = b // 10 

print(sum(l))



