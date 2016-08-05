oldSalary = float(input())
newSalary = 0.0
percentual = 0

if oldSalary <= 400:
    newSalary = oldSalary * 1.15
    percentual = 15
elif oldSalary <= 800:
    newSalary = oldSalary * 1.12
    percentual = 12
elif oldSalary <= 1200:
    newSalary = oldSalary * 1.1
    percentual = 10
elif oldSalary <= 2000:
    newSalary = oldSalary * 1.07
    percentual = 7
else:
    newSalary = oldSalary * 1.04
    percentual = 4

reajuste = newSalary - oldSalary

print("Novo salario: %.2f" %newSalary)
print("Reajuste ganho: %.2f" %reajuste)
print("Em percentual: %i %%" %percentual)
