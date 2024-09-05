# Python Program to Find Prime Numbers in a Given Range

prime = int(input('Enter a Limit:'))

for i in range(2, prime+1):
    count = 0
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            count += 1
    if count<=0:
        print(i)