# Python Program to Print Binary Equivalent of an Integer using Recursion

# Method-1: Print Binary Equivalent of an Integer using Recursion

# l=[]
# def convert(n):
#     if n==0:
#         return l
#     dig = n % 2
#     l.append(dig)
#     convert(n // 2)
#     return l

# n = int(input('Enter a num:'))
# convert(n)

# l.reverse()

# print('Binary equivalent is:')
# for i in l:
#     print (i, end=' ')


# ================================================================

# Method-1: Print Binary Equivalent of an Integer without Recursion

n = int(input('Enter a num:'))
l=[]

while (n != 0):
    dig = n % 2
    l.append(dig)
    rem = n // 2
    n = rem

l.reverse()
print('Binary equivalent is: ', end='')
for i in l:
    print(i, end='')



