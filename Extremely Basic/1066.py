n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
even = 0
odd = 0
positive = 0
negative = 0

if n1 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if n1 > 0:
    positive = positive + 1
elif n1 < 0:
    negative = negative + 1

if n2 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if n2 > 0:
    positive = positive + 1
elif n2 < 0:
    negative = negative + 1

if n3 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if n3 > 0:
    positive = positive + 1
elif n3 < 0:
    negative = negative + 1

if n4 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if n4 > 0:
    positive = positive + 1
elif n4 < 0:
    negative = negative + 1

if n5 % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if n5 > 0:
    positive = positive + 1
elif n5 < 0:
    negative = negative + 1

print('%i valor(es) par(es)' %even)
print('%i valor(es) impar(es)' %odd)
print('%i valor(es) positivo(s)' %positive)
print('%i valor(es) negativo(s)' %negative)
