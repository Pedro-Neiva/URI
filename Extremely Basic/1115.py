readNext = True

while readNext:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x == 0 or y == 0:
        readNext = False
    else:
        if y > 0:
            if x >0:
                print('primeiro')
            else:
                print('segundo')
        else:
            if x > 0:
                print('quarto')
            else:
                print('terceiro')
