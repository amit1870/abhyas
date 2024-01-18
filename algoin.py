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


def is_perfect_integer(number):
    t_number = number
    while t_number != 0 :
        t_mod = t_number % 10

        if t_mod == 0 or (t_mod != 0 and number % t_mod != 0):
            break
        elif t_mod != 0 and number % t_mod == 0:
            t_number = t_number // 10

    return t_number == 0

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
    f_max = nlist[0]
    s_max = f_max

    for item in nlist[1:]:
        if item > f_max:
            s_max = f_max
            f_max = item

        elif item > s_max:
            s_max = item
            
    return s_max
