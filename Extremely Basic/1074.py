from array import *

myArray = array('i', [])

n = int(input())

while n > 0:
    x = int(input())
    myArray.append(x)
    n = n - 1

for i in myArray:
    if i == 0:
        print('NULL')
    elif i > 0:
        if i % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    else:
        if i % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
