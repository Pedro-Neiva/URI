average = 0.0
n = int(input())

while n > 0:
    i1, i2, i3 = input().split()
    i1 = float(i1)
    i2 = float(i2)
    i3 = float(i3)
    average = ((i1 * 2) + (i2 * 3) + (i3 * 5)) / 10
    print('%.1f' %average)
    n = n - 1
