# Python Program to Find the LCM of Two Numbers

a = int(input('Enter a:'))
b = int(input('Enter b:'))

if a < b:
    min1 = b
else:
    min1 = a

while(1):
    if(min1%a==0 and min1%b==0):
        print('LCM is', min1)
        break
    min1 += 1



    