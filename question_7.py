def fibonacci(num):
    fib = [0, 1]
    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:num]

result = fibonacci(10)
print(result)