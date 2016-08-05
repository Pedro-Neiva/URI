n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
count = 0
average = 0.0
total = 0.0

if n1 > 0:
    count = count + 1
    total = total + n1

if n2 > 0:
    count = count + 1
    total = total + n2

if n3 > 0:
    count = count + 1
    total = total + n3

if n4 > 0:
    count = count + 1
    total = total + n4

if n5 > 0:
    count = count + 1
    total = total + n5

if n6 > 0:
    count = count + 1
    total = total + n6

print('%i valores positivos' %count)

if total > 0:
    average = total / count
    print('%.1f' %average)
