x = int(input())
y = int(input())
firstNumber = 0
lastNumber = 0
count = 0

if x > y:
    firstNumber = y
    lastNumber = x
elif x < y:
    firstNumber = x
    lastNumber = y

while firstNumber < (lastNumber - 1):
    firstNumber = firstNumber + 1
    if firstNumber % 2 != 0:
        count = count + firstNumber

print(count)
