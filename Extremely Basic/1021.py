value = float(input())
value = value * 100
value = int(value)
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda100 = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda5 = 0
moeda1 = 0

while value >= 10000:
    value = value - 10000
    nota100 = nota100 + 1

while value >= 5000:
    value = value - 5000
    nota50 = nota50 + 1

while value >= 2000:
    value = value - 2000
    nota20 = nota20 + 1

while value >= 1000:
    value = value - 1000
    nota10 = nota10 + 1

while value >= 500:
    value = value - 500
    nota5 = nota5 + 1

while value >= 200:
    value = value - 200
    nota2 = nota2 + 1

while value >= 100:
    value = value - 100
    moeda100 = moeda100 + 1

while value >= 50:
    value = value - 50
    moeda50 = moeda50 + 1

while value >= 25:
    value = value - 25
    moeda25 = moeda25 + 1

while value >= 10:
    value = value - 10
    moeda10 = moeda10 + 1

while value >= 5:
    value = value - 5
    moeda5 = moeda5 + 1

while value >= 1:
    value = value - 1
    moeda1 = moeda1 + 1

print("NOTAS:\n%i nota(s) de R$ 100.00\n%i nota(s) de R$ 50.00\n%i nota(s) de R$ 20.00\n%i nota(s) de R$ 10.00\n%i nota(s) de R$ 5.00\n%i nota(s) de R$ 2.00\nMOEDAS:\n%i moeda(s) de R$ 1.00\n%i moeda(s) de R$ 0.50\n%i moeda(s) de R$ 0.25\n%i moeda(s) de R$ 0.10\n%i moeda(s) de R$ 0.05\n%i moeda(s) de R$ 0.01" %(nota100, nota50, nota20, nota10, nota5, nota2, moeda100, moeda50, moeda25, moeda10, moeda5, moeda1))
