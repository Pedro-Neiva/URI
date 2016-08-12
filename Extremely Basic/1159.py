while True:
    x = int(input())
    if x == 0:
        break
    total = 0
    count = 0

    while count < 5:
        if x % 2 == 0:
            total = total + x
            count = count + 1
        x = x + 1
    print(total)
