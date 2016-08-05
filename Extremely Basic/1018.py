total = int(input())
N = total
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

while N >= 100:
    N = N - 100
    nota100 = nota100 + 1

while N >= 50:
    N = N - 50
    nota50 = nota50 + 1

while N >= 20:
    N = N - 20
    nota20 = nota20 + 1

while N >= 10:
    N = N - 10
    nota10 = nota10 + 1

while N >= 5:
    N = N - 5
    nota5 = nota5 + 1

while N >=2:
    N = N - 2
    nota2 = nota2 + 1

while N >= 1:
    N = N - 1
    nota1 = nota1 + 1

print("%i\n%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00" %(total, nota100, nota50, nota20, nota10, nota5, nota2, nota1))
