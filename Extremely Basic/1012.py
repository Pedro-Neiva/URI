A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
triangulo = (A * C) / 2
circulo = 3.14159 * C * C
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B
print("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(triangulo, circulo, trapezio, quadrado, retangulo))
