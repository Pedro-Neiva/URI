i = 0.0
j = 1.0
count3 = 0
count5 = 0

while i <= 2.0:
    while count3 < 3:
        if count5 % 5 == 0:
            print('I=%.0f J=%.0f' %(i, j))
            count5 = 0
        else:
            print('I=%.1f J=%.1f' %(i, j))
        j = j + 1
        count3 = count3 + 1
    i = i + 0.2
    j = j - 3 + 0.2
    count3 = 0
    count5 = count5 + 1
