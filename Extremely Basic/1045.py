ladoA, ladoB, ladoC = input().split()
ladoA = float(ladoA)
ladoB = float(ladoB)
ladoC = float(ladoC)
a = max(ladoA, ladoB, ladoC)
c = min(ladoA, ladoB, ladoC)
b = 0

if a == ladoA and c == ladoC:
    b = ladoB
elif a == ladoC and c == ladoA:
    b = ladoB
elif a == ladoA and c == ladoB:
    b = ladoC
elif a == ladoB and c ==ladoA:
    b = ladoC
elif a == ladoB and c == ladoC:
    b = ladoA
elif a == ladoC and c == ladoB:
    b = ladoA

#print("A = %.1f\nB = %.1f\nC = %.1f" %(a, b, c))

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
        if a * a == b * b + c * c:
            print("TRIANGULO RETANGULO")

        if a * a > b * b + c * c:
            print("TRIANGULO OBTUSANGULO")

        if a * a < b * b + c * c:
            print("TRIANGULO ACUTANGULO")

        if a == b and a == c:
            print("TRIANGULO EQUILATERO")

        if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("TRIANGULO ISOSCELES")
