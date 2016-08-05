rabbit = 0
rat = 0
frog = 0
total = 0


n = int(input())

while n > 0:
    quantity, animal = input().split()
    quantity = int(quantity)
    total = total + quantity
    if animal == 'C':
        rabbit = rabbit + quantity
    elif animal == 'R':
        rat = rat + quantity
    elif animal == 'S':
        frog = frog + quantity
    n = n - 1

print('Total: %i cobaias' %total)
print('Total de coelhos: %i' %rabbit)
print('Total de ratos: %i' %rat)
print('Total de sapos: %i' %frog)
print('Percentual de coelhos: %.2f %%' %((rabbit / total) * 100))
print('Percentual de ratos: %.2f %%' %((rat / total) * 100))
print('Percentual de sapos: %.2f %%' %((frog / total) * 100))
