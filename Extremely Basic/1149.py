a, n = input().split()
a = int(a)
n = int(n)
soma = 0

while n <= 0:
    n = int(input())

while n > 0:
    soma = soma + a
    a = a + 1
    n = n - 1

print(soma)
