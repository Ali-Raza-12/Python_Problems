# Python Program to Find Product of Two Numbers using Recursion

def product(a,b):
    if a<b:
        return product(b,a)
    elif(b!=0):
        return (a+product(a,b-1))
    else:
        return 0

a = int(input('Enter A:'))
b = int(input('Enter B:'))

product(a,b)
print("Product is: ",product(a,b))