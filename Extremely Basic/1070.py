n = int(input())
count = 0

while count < 6:
    if n % 2 != 0:
        print(n)
        count = count + 1
        n = n + 1
    else:
        n = n + 1
