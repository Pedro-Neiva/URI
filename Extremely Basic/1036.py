import math

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = (B * B) - (4 * A * C)

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    raiz1 = ((B * -1) + (math.sqrt(delta))) / (2 * A)
    raiz2 = ((B * -1) - (math.sqrt(delta))) / (2 * A)
    print("R1 = %.5f\nR2 = %.5f" %(raiz1, raiz2))
