# Python Program to Find Whether a Number is a Power of Two


def square(n):
    if n < 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1


n = int(input('Enter a number:'))

if square(n):
    print(f'{n} is power of 2')
else:
    print(f'{n} is not a power of 2')