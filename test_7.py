def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


for _ in fibonacci(10):
    print(_, end=' ')

print('\n', sum(fibonacci(10)))