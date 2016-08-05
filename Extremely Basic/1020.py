age = int(input())
year = 0
month = 0
day = 0

while age >= 365:
    age = age - 365
    year = year + 1

while age >= 30:
    age = age - 30
    month = month + 1

while age > 0:
    age = age - 1
    day = day + 1

print("%i ano(s)\n%i mes(es)\n%i dia(s)" %(year, month, day))
