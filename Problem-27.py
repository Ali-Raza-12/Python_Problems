# Python Program to Print the Natural Numbers Summation Pattern

num = int(input('Enter a number:'))

for i in range(1, num+1):
    a=[]
    for j in range(1, i+1):
        print(j, sep=' ', end=' ')
        a.append(j)
        if j < i:
            print('+', sep=' ', end=' ')
    print('=', sum(a))

print()

    