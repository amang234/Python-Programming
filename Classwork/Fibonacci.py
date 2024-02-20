def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Generate the first 10 Fibonacci numbers
n = 10
fib_sequence = fibonacci(n)
print(fib_sequence)
