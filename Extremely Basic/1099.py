n = int(input())
beginning = 0
end = 0

while n > 0:
    total = 0
    x, y = input().split()
    x = int(x)
    y = int(y)
    beginning = min(x, y)
    beginning = beginning + 1
    end = max(x, y)
    while beginning < end:
        if beginning % 2 != 0:
            total = total + beginning
        beginning = beginning + 1
    print(total)
    n = n - 1
