def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        if i != n - 1:
            print('%s ' %a, end='')
            temp = a
            a = b
            b = temp + b
        else:
            print(a)
    return a

n = int(input())
fibonacci(n)
