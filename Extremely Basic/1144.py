n = int(input())
base = 1
square = 1
cube = 1

while base <= n:
    square = base * base
    cube = square * base
    print('%i %i %i' %(base, square, cube))
    square = square + 1
    cube = cube + 1
    print('%i %i %i' %(base, square, cube))
    base = base + 1
