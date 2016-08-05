from array import *

inInterval = 0
outInterval = 0
myArray = array('i', [])
n = int(input())

while n > 0:
    x = int(input())
    myArray.append(x)
    n = n - 1

for i in myArray:
    if i >= 10 and i <= 20:
        inInterval = inInterval + 1
    else:
        outInterval = outInterval + 1 

print('%i in' %inInterval)
print('%i out' %outInterval)
