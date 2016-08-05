n = int(input())
base = 1
square = 1
cube = 1

while base <= n:
    square = base * base
    cube = base * square
    print('%i %i %i' %(base, square, cube))
    base = base + 1
