readNext = True
count = 0
average = 0.0

while readNext:
    grade = int(input())
    if grade < 0:
        readNext = False
        break
    count = count + 1
    average = average + grade

average = average / count
print("%.2f" %average)
