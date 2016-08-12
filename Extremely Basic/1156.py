numerador = 1.0
denominador = 1.0
total = 0.0

while numerador <= 39:
    total = total + (numerador / denominador)
    numerador = numerador + 2
    denominador = denominador * 2

print("%.2f" %total)
