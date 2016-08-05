position = 0
n = 1
highest = 0

while n <= 100:
    x = int(input())
    if x > highest:
        highest = x
        position = n
    n = n + 1

print(highest)
print(position)
