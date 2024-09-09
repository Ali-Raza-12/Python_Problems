# Python Program to Print Numbers in a Range Without using Loops

def rec(upp):
    if(upp > 0):
        rec(upp-1)
        print(upp)
    
upp = int(input('Enter a uper limit:'))
rec(upp)
