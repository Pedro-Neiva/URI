readNext = True
vitoriasGremio = 0
vitoriasInter = 0
empates = 0
grenais = 0

while readNext:
    golsInter, golsGremio = input().split()
    golsGremio = int(golsGremio)
    golsInter = int(golsInter)
    grenais = grenais + 1
    if golsGremio == golsInter:
        empates = empates + 1
    elif golsGremio > golsInter:
        vitoriasGremio = vitoriasGremio + 1
    else:
        vitoriasInter = vitoriasInter + 1
    print('Novo grenal (1-sim 2-nao)')
    novoJogo = input()
    if novoJogo == '2':
        readNext = False

print('%i grenais' %grenais)
print('Inter:%i' %vitoriasInter)
print('Gremio:%i' %vitoriasGremio)
print('Empates:%i' %empates)

if vitoriasGremio == vitoriasInter:
    print('Nao houve vencedor')
elif vitoriasGremio > vitoriasInter:
    print('Gremio venceu mais')
else:
    print('Inter venceu mais')
