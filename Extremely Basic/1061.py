lixo, diaInicial = input().split()
horaInicial, minutoInicial, segundoInicial = input().split(' : ')
lixo, diaFinal = input().split()
horaFinal, minutoFinal, segundoFinal = input().split(' : ')
totalInicial = 0
totalFinal = 0
diaInicial = int(diaInicial)
horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
segundoInicial = int(segundoInicial)
diaFinal = int(diaFinal)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)
segundoFinal = int(segundoFinal)
total = 0
dias = 0
horas = 0
minutos = 0
segundos = 0

totalInicial = (horaInicial * 3600) + (minutoInicial * 60) + segundoInicial
totalFinal = (horaFinal * 3600) + (minutoFinal * 60) + segundoFinal
total = (diaFinal - diaInicial) * 24 * 60 * 60
total = total + totalFinal - totalInicial

while total >= 86400:
    total = total - 86400
    dias = dias + 1

while total >= 3600:
    total = total - 3600
    horas = horas + 1

while total >= 60:
    total = total - 60
    minutos = minutos + 1

segundos = total

print('%i dia(s)' %dias)
print('%i hora(s)' %horas)
print('%i minuto(s)' %minutos)
print('%i segundo(s)' %segundos)
