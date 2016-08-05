x, y = input().split()
x = int(x)
y = int(y)
beginning = 1
count = 1

while beginning <= y:
    if count < x:
        print('%i ' %beginning, end='')
        beginning = beginning + 1
        count = count + 1
    else:
        print('%i' %beginning)
        beginning = beginning + 1
        count = 1
