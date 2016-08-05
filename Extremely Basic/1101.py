readNext = True

while readNext:
    total = 0
    m, n = input().split()
    m = int(m)
    n = int(n)
    if m <= 0 or n <= 0:
        readNext = False
        break
    else:
        beginning = min(m, n)
        end = max(m, n)
        while beginning <= end:
            print('%i ' %beginning, end='')
            total = total + beginning
            beginning = beginning + 1
        print('Sum=%i' %total)
