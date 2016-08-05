inicio, fim = input().split()
inicio = int(inicio)
fim = int(fim)

if fim > inicio:
    total = fim - inicio
elif inicio > fim:
    total = 24 - inicio + fim
else:
    total = 24

print("O JOGO DUROU %i HORA(S)" %total)
