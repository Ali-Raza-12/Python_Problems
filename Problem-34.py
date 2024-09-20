# Python Program to Print All Possible Combinations of Three Digits

# a = int(input('Enter a digit A:'))
# b = int(input('Enter a digit B:'))
# c = int(input('Enter a digit C:'))

# d = []

# d.append(a)
# d.append(b)
# d.append(c)

# for i in range(0,3):
#     for j in range(0, 3):
#         for k in range(0, 3):
#             if (i!=j & j!=k & k!=i):
#                 print(d[i], d[j], d[k])

# ==================================================

# using permutation

from itertools import permutations

numbers = input('Enter numbers seperated by spaces: ').split()

numbers = [int(num) for num in numbers]

tot_perm = 0
for perm in permutations(numbers):
    print(perm)
    tot_perm += 1

print(tot_perm)
    