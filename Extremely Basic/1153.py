def factorial(n):
    total = 1
    while (n > 1):
        total = total * n
        n = n - 1
    return total

n = int(input())
print(factorial(n))
