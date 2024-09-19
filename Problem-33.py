# Python Program to Find All Perfect Squares in the Given Range and sum of digits less than 10 


l = int(input('Enter lower limit:'))
u = int(input('Enter upper limit:'))

a = []

a = [ x for x in range(l, u+1) if (int(x**0.5))**2 == x and sum(list(map(int, str(x)))) < 10 ]

print(a)