code, quantity = input().split()
code = int(code)
quantity = int(quantity)
total = 0.0

if code == 1:
    total = quantity * 4.00
elif code == 2:
    total = quantity * 4.50
elif code == 3:
    total = quantity * 5.00
elif code == 4:
    total = quantity * 2.00
elif code == 5:
    total = quantity * 1.50

print("Total: R$ %.2f" %total)
