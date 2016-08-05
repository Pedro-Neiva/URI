readNext = True

while readNext:
    n = int(input())
    if n == 0:
        readNext = False
    else:
        beginning = 1
        while beginning <= n:
            if beginning == n:
                print('%i' %beginning)
            else:
                print('%i ' %beginning, end='')
            beginning = beginning + 1
