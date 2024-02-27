def is_pallindrom(string):
    reverse_index = len(string) - 1
    forward_index = 0

    while forward_index < reverse_index:
        if string[forward_index] != string[reverse_index]:
            return False
        forward_index += 1
        reverse_index -= 1

    return True


def get_number_sum(number):
    total = 0

    while number != 0:
        total = total + (number % 10)
        number = number // 10

    return total

def reverse_number(number):
    total = 0
    while number != 0:
        digit = (number % 10)
        total =  total * 10 + digit

        number //= 10

    return total


def is_perfect_integer(number):
    while number != 0 :
        digit = number % 10

        if digit == 0 or (digit != 0 and number % digit != 0):
            break
        elif digit != 0 and number % digit == 0:
            number = number // 10

    return number == 0

def sum_list(func):
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))

    return wrapper


@sum_list
def fibo_series(n_range):
    series = [0,1]

    while n_range > 0:
        series.append(series[-2] + series[-1])
        n_range -= 1

    return series


def count_chars(word):
    prev_crt = word[0]
    count = 1
    counts = []
    for crt in word[1:]:
        if crt == prev_crt:
            count += 1
        elif crt != prev_crt:
            counts.append('{}{}'.format(prev_crt, count))
            count = 1
            prev_crt = crt

    return counts.append('{}{}'.format(prev_crt, count))


def get_prefix(words):
    prefix = words[0]
    for word in words[1:]:
        for i, crt in enumerate(word):
            if i < len(prefix) and crt == prefix[i]:
                continue
            else:
                prefix = prefix[:i]
                break

    return prefix


def second_max(nlist):
    fst_max = nlist[0]
    snd_max = fst_max
    snd_index = 0

    for index, item in enumerate(nlist[1:], start=1):
        if item > fst_max:
            snd_max = fst_max
            fst_max = item
            snd_index = index

        elif item != fst_max and item > snd_max:
            snd_max = item
            snd_index = index

    return snd_index, snd_max


def read_file(filepath):
    count = 0
    line_count = 0
    with open(filepath) as fp:
        for line in fp:
            line_count += 1
            for ch in line:
                if ch.isupper():
                    count += 1

    return count, line_count

def fibonaci(n):
    if n <= 1:
        return n
    return n + fibonaci(n-1)

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)




