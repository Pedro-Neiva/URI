n = int(input())
count = 1
square = 0

while count <= n:
    if count % 2 == 0:
        square = count * count
        print('%i^2 = %i' %(count, square))
    count = count + 1
