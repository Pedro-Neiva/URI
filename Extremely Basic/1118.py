readNext = True
n1 = 100.0
n2 = 100.0
media = 0.0


while readNext:
    n1 = float(input())
    while n1 < 0.0 or n1 > 10.0:
        print('nota invalida')
        n1 = float(input())
    n2 = float(input())
    while n2 < 0.0 or n2 > 10.0:
        print('nota invalida')
        n2 = float(input())
    media = (n1 + n2) / 2
    print('media = %.2f' %media)
    print('novo calculo (1-sim 2-nao)')
    n1 = 100.0
    n2 = 100.0
    novoCalculo = input()
    while novoCalculo != '1' and novoCalculo != '2':
        print('novo calculo (1-sim 2-nao)')
        novoCalculo = input()
    if novoCalculo == '2':
        readNext = False
