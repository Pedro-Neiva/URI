horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)
totalInicial = horaInicial * 60 + minutoInicial
totalFinal = horaFinal * 60 + minutoFinal
total = abs(totalInicial - totalFinal)
horas = 0
minutos = 0

if horaInicial == horaFinal and minutoFinal == minutoInicial:
    horas = 24
else:
    if horaFinal > horaInicial:
        horas = horaFinal - horaInicial
    elif horaInicial > horaFinal:
        horas = 24 - horaInicial + horaFinal

    if minutoFinal > minutoInicial:
        minutos = minutoFinal - minutoInicial
    elif minutoInicial > minutoFinal:
        minutos = 60 - minutoInicial + minutoFinal
        if horaInicial == horaFinal and minutoInicial > minutoFinal:
            horas = 24
        horas = horas - 1



print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(horas, minutos))
