# Python Program to Read a Number n and Compute n+nn+nnn

n = int(input('Enter a num:'))

temp = str(n)
temp1 = temp + temp
temp2 = temp + temp + temp

add = int(n) + int(temp1) + int(temp2)

print(add)