readNext = True

while readNext:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == y:
        readNext = False
        break
    else:
        if x < y:
            print('Crescente')
        else:
            print('Decrescente')
