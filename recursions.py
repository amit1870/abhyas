# simple recusive functions

def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n

    return n + fibonacci(n-1)


n = 4
result = fibonacci(n)
print(result)
