# simple recusive functions with limit


def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n

    return n + fibonacci(n-1)

def reverse_word(word):
    if len(word) == 0:
        return word


    return reverse(word[1:]) + word[0]

