soma = 0
x = int(input())
y = int(input())
beginning = min(x, y)
end = max(x, y)

while beginning <= end:
    if beginning % 13 != 0:
        soma = soma + beginning
    beginning = beginning + 1

print(soma)
