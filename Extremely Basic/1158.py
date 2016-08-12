n = int(input())

while n > 0:
    total = 0
    x, y = input().split()
    x = int(x)
    y = int(y)
    n = n - 1

    while y > 0:
        if x % 2 != 0:
            total = total + x
            y = y - 1
        x = x + 1

    print(total)
