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


def fibo_series(n_range):
    series = [0,1]

    while n_range > 0:
        series.append(series[-2] + series[-1])
        n_range -= 1

    return series

