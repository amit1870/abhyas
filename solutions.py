# module will contain some simple/linear approach for solutions
# what i can think and implement

VSTRING = "radhakrisshnnaaa"
NUMBER  = 12345
PERFECT_NUMBER = 28
WORDS = ['patel', 'patelamit', 'patelsunil', 'pateamit']
NUMBERS = [12, 14, 98, 87, 109, 97, 98, 98, 97, 109]

def is_palindrom(vstring):
    # use two pointers to iterate
    # one forward pointer and one backward pointer
    # they should not cross each other

    FLAG = True

    if len(vstring) < 2:
        return FLAG

    forward_pointer = 0
    backward_pointer = len(vstring) - 1

    while FLAG and forward_pointer < backward_pointer:
        if vstring[forward_pointer] == vstring[backward_pointer]:
            forward_pointer += 1
            backward_pointer -= 1
        else:
            FLAG = False

    return FLAG


def sum_number(number):
    total = 0

    while number != 0:
        digit = number % 10
        total = total + digit

        number //= 10

    return total

def reverse_number(number):
    rnumber = 0

    while number != 0 :
        digit = number % 10
        rnumber = rnumber * 10 + digit

        number //= 10

    return rnumber

def get_factors(number):
    factors = [1]

    for i in range(2, number// 2 + 1):
        if number % i == 0:
            factors.append(i)

    return factors

def is_perfect_number(number):
    # perfect number is number where factor of number sums number
    # 28 = 1 2 4 7 14 = 28
    # 6  = 1 2 3 = 6

    return sum(get_factors(number)) == number


def fibo_series(n):
    series = [0,1]
    while n > 0:
        series.append(series[-1] + series[-2])
        n -= 1

    return series

def factorial(n):
    total = 1

    while n != 1:
        total *= n
        n -= 1

    return total

def rfactorial(n):
    if n < 2:
        return 1

    return n * rfactorial(n - 1)


def continuous_string_count(vstring):
    string_with_count = []

    if len(vstring) == 0:
        return " ".join(string_with_count)

    count = 1
    prvchar = vstring[0]
    for ch in vstring[1:]:
        if ch == prvchar:
            count += 1
        else:
            string_with_count.append(prvchar)
            string_with_count.append(str(count))

            count = 1
            prvchar = ch

    string_with_count.append(prvchar)
    string_with_count.append(str(count))


    return " ".join(string_with_count)


def get_prefix_word(words):
    prefix = words[0]
    for word in words[1:]:
        for index, ch in enumerate(word):
            if index < len(prefix) and ch == prefix[index]:
                continue
            else:
                prefix = prefix[:index]
                break

    return prefix

def second_max_with_index(numbers):

    if len(numbers) < 2:
        return numbers

    highest = numbers[0]
    second_highest = highest
    second_highest_index = 0

    for index, number in enumerate(numbers[1:], start=1):
        if number > highest:
            second_highest = highest
            second_highest_index = second_highest_index
            highest = number

        elif number > second_highest and number < highest:
            second_highest = number
            second_highest_index = index

    return second_highest_index, second_highest


if __name__ == "__main__":
    print(second_max_with_index(NUMBERS))

