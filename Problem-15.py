# Python Program to Check if a Date is Valid and Print the Incremented Date if it is

date = input('Enter Date in dd-mm-yyyy format:')
dd, mm, yy = map(int, date.split('-'))

if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
    max1 = 31
elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
    max1 = 30
elif ((yy % 4 == 0 and yy % 100 != 0) or yy % 400 == 0 ):
    max1 = 29
else:
    max1 = 28

if (mm < 1 or mm > 12):
    print('Invalid Date')
elif (dd < 1 or dd > max1):
    print('Invalid Date')
else:
    if (dd == max1 and mm != 12):
        dd = 1
        mm += 1
    elif (dd == 31 or mm == 12):
        dd = 1
        mm = 1
        yy += 1
    else:
        dd += 1
    print('The incremented date is:', dd, '-', mm, '-', yy)


