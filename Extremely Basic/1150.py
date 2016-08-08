x = int(input())
z = int(input())
total = 0
count = 0

while z <= x:
    z = int(input())

while total <= z:
    total = total + x
    x = x + 1
    count = count + 1

print(count)
