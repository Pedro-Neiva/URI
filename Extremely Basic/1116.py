n = int(input())
divisao = 0.0

while n > 0:
    x, y = input().split()
    x = float(x)
    y = float(y)
    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print('%.1f' %divisao)
    n = n - 1
