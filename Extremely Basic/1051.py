salary = float(input())
tax = 0.0
taxFinished = False

if salary <= 2000:
    print("Isento")
    taxFinished = True

if salary > 4500 and taxFinished == False:
    tax = tax + 1000 * 0.08
    tax = tax + 1500 * 0.18
    tax = tax + (salary - 4500) * 0.28
    print("R$ %.2f" %tax)
    taxFinished = True

if salary > 3000 and taxFinished == False:
    tax = tax + 1000 * 0.08
    tax = tax + (salary - 3000) * 0.18
    print("R$ %.2f" %tax)
    taxFinished = True

if salary > 2000 and taxFinished == False:
    tax = tax + (salary - 2000) * 0.08
    print("R$ %.2f" %tax)
    taxFinished = True
