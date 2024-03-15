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
                if ord(ch) in range(64,91):
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

def matrix_sum_tool(matrix_X, matrix_Y, matrix_Z):
    import itertools
    matrix_sum = []
    for index in range(len(matrix_X)):
        if type(matrix_X[index]) != type([]):
            matrix_X[index] = [matrix_X[index]]
        if type(matrix_Y[index]) != type([]):
            matrix_Y[index] = [matrix_Y[index]]
        if type(matrix_Z[index]) != type([]):
            matrix_Z[index] = [matrix_Z[index]]

        zipped = list(itertools.zip_longest(matrix_X[index],
                                            matrix_Y[index],
                                            matrix_Z[index],
                                            fillvalue=0
                                            ))

        sum_item = []
        for item in zipped:
            sum_item.append(sum(item))

        matrix_sum.append(sum_item)

    return matrix_sum

def matrix_sum(matrix_X, matrix_Y, matrix_Z):
    matrix = []
    max_length = max(len(matrix_X), len(matrix_Y), len(matrix_Z))


    for index in range(max_length):
        rowX = matrix_X[index]
        rowY = matrix_Y[index]
        rowZ = matrix_Z[index]

        if type(rowX) != type([]):
            rowX = [rowX]

        if type(rowY) != type([]):
            rowY = [rowY]

        if type(rowZ) != type([]):
            rowZ = [rowZ]

        row_length = max(len(rowX), len(rowY), len(rowZ))

        sum_rows = []
        for rindex in range(row_length):
            total = 0
            if rindex < len(rowX):
                total += rowX[rindex]

            if rindex < len(rowY):
                total += rowY[rindex]

            if rindex < len(rowZ):
                total += rowZ[rindex]

            sum_rows.append(total)

        matrix.append(sum_rows)

    return matrix


matrix_X = [[1,2,3], [4,5,6], [7,8,9]]
matrix_Y = [[9,8,7], [6,5,4], [3,2,1]]
matrix_Z = [1, [1,2], [1,2,3]]
matrix = [[11,10,10], [11,12,10], [11,12,13]]
matrix = matrix_sum(matrix_X, matrix_Y, matrix_Z)


def get_logo(company):
    from collections import defaultdict

    char_dict = defaultdict(int)
    for char in company:
        char_dict[char] += 1

    char_items = char_dict.items()
    char_items = sorted(char_items, key=lambda item : item[0], reverse=False)
    char_items = sorted(char_items, key=lambda item : item[1], reverse=False)
    char_items = sorted(char_items, key=lambda item : item[1], reverse=True)


    for pair in char_items[:3]:
        print(pair[0], pair[1])


def count_set(nlist, maxlimit):
    count = 0
    traversed = []
    for i in range(len(nlist)):
        for j in range(len(nlist)):
            for k in range(len(nlist)):
                if i != j and i != k and j != k:
                    triplet = sorted([nlist[i], nlist[j], nlist[k]])
                    if triplet not in traversed and sum(triplet) < maxlimit:
                        count += 1
                        traversed.append(triplet)
                        # print(traversed)

    return count


nlist = [10, 5, 8, 15, 11, 7]
maxlimit = 25

set_count = count_set(nlist, maxlimit)
# print(set_count)


class Tanker:
    tankers = []
    def __init__(self, capacity):
        self.capacity = capacity
        self.tankers.append(capacity)

    def required_tankers(self, day_capacity):
        tankers = []

        sorted_tankers = sorted(self.tankers, reverse=True)
        findex = 0
        rindex = -1

        while day_capacity > 0 and findex < len(sorted_tankers) and rindex >= - len(sorted_tankers):
            tank = sorted_tankers[findex]
            if day_capacity <= sorted_tankers[rindex]:
                tank = sorted_tankers[rindex]
                rindex -= 1


            day_capacity -= tank
            findex += 1
            tankers.append(tank)

        return tankers

tanks = [50,45,10,70,60,20]
tobj = Tanker(50)
for tank in tanks[1:]:
    Tanker(tank)



def search_substring(slist):
    if len(slist) < 3:
        return ''

    paired = []
    for sitem in slist:
        for ditem in slist:
            if sitem != ditem:
                if sitem + ditem in slist:
                    paired.append(sitem + ditem)

    return " ".join(paired)









