N = int(input())
hours = 0
minutes = 0
seconds = 0

while N >= 3600:
    N = N -3600
    hours = hours + 1

while N >= 60:
    N = N - 60
    minutes = minutes + 1

while N > 0:
    N = N - 1
    seconds = seconds + 1

print("%i:%i:%i" %(hours, minutes, seconds))
