# Method:Python Program to Calculate Grade of a Student

sub1 = int(input('Enter nunb in sub1:'))
sub2 = int(input('Enter nunb in sub2:'))
sub3 = int(input('Enter nunb in sub3:'))
sub4 = int(input('Enter nunb in sub4:'))
sub5 = int(input('Enter nunb in sub5:'))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if (avg >= 90):
    print('Your Grade is A')
elif (avg >= 80 and avg < 90):
    print('Your Grade is B')
elif (avg >= 70 and avg < 80):
    print('Your Grade is C')
elif (avg >= 60 and avg < 70):
    print('Your Grade is D')
elif (avg >= 50 and avg < 60):
    print('Your Grade is P')
else:
    print('Fail')