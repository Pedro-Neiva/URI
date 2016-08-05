from array import array

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
arrayDesordenado = array("i",[a, b, c])

menor = min(a, b , c)
maior = max(a, b, c)

print(menor)
if menor < a and maior > a:
    print(a)
elif menor < b and maior > b:
    print(b)
else:
    print(c)
print(str(maior) + "\n")



for value in arrayDesordenado:
    print(value)
