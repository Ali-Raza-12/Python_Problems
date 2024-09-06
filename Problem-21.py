# Python Program to Check whether a Number is Prime or Not using Recursion

def check(n, div = None):
    if div == None:
        div = n - 1
    while div >= 2:
        if n % 2 == 0:
            print('Not a Prime number.')
            return False
        else:
            return check(n , div-1 )
    else:
        print('Prime Number.')
        return False

n = int(input('Enter a num:'))
check(n)