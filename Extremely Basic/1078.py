n = int(input())
count = 1
multiplication = 0

while count <= 10:
    multiplication = count * n
    print('%i x %i = %i' %(count, n, multiplication))
    count = count + 1
