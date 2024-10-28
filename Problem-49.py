abc = input('Enter string:')

final = ''

for i in range(len(abc)):
    if i % 2 == 0:
        final = final + abc[i]
    
print('Modified string is:', final)