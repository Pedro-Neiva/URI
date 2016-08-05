x = int(input())
y = int(input())
beginning = min(x, y)
beginning = beginning + 1
end = max(x, y)

while beginning < end:
    if (beginning % 5 == 2) or (beginning % 5 == 3):
        print(beginning)
    beginning = beginning + 1
