media = 0.0
count = 0

while count < 2:
    n = float(input())
    if n < 0 or n > 10.0:
        print('nota invalida')
    else:
        media = media + n
        count = count + 1

media = media / 2
print('media = %.2f' %media)
