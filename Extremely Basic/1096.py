i = 1
j = 7
count = 0

while i <= 9:
    if count < 3:
        print('I=%i J=%i' %(i, j))
        j = j - 1
        count = count + 1
    else:
        i = i + 2
        j = 7
        count = 0
