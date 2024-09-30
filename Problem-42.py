# Python Program to Find Simple Interest

principle = float(input('Enter amount you invested:'))
time = int(input('Enter year:'))
rate = float(input('Enter rate:'))

simple_interest = (principle * time * rate)/100

print('The simple interest is:', simple_interest)
