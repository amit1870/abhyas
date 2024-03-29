# decorator : allow to extend/modify a function without touching original function
#           : inner function allow to pass argument to original function
#           : returned inner function allow to take argument from outside of outer function
#           : variable binding to inner function
# iterator  : which implements two method __iter__() and __next__().
# generator : allow to create iterator in functional style.
# generator : no need to provide __iter__ and __next__ method.
# function  : function are first class objects and objects can assigned/returned.

# decorator without arguments

def jay_sitaram(func):
    def wrapper():
        return [f"say sitaram {name}" for name in func()]

    return wrapper

@jay_sitaram
def get_names():
    return ['sachin', 'sunil', 'rajesh', 'brijesh', 'durgesh', 'amit', 'rajkumar']


names = get_names()
print(names)

# decorator with arguments

def read_radha(func):
    def wrapper(varn):
        if varn == 'BMH':
            return [f"{rishi} leads bharat" for rishi in func(varn)]

        elif varn == 'KSH':
            return [f"{ksh} protect bharat" for ksh in func(varn)]

        elif varn == 'VSH':
            return [f"{vsh} prosper bharat" for vsh in func(varn)]

        return [f"{sdh} does sitaram" for sdh in func(varn)]


    return wrapper

@read_radha
def do_dharm(varn):
    if varn == 'BMH':
        return ['guruvar', 'maharishi', 'vashithaji', 'vishwamitramuni', 'jabali', 'kashyap']

    elif varn == 'KSH':
        return ['sitaram', 'radhakrishna', 'lakshman', 'bharat', 'satrudhan']

    elif varn == 'VSH':
        return ['madhav', 'chaitnya', 'mahaprabhu', 'vallbha']

    return ['amit', 'sachin', 'sunil', 'rajesh', 'rajkumar', 'brijesh']


bmh = do_dharm('BMH')
ksh = do_dharm('KSH')
vsh = do_dharm('VSH')
sdh = do_dharm('SDH')

print(bmh)
print(ksh)
print(vsh)
print(sdh)

# decorator without @syntax

def generate_number(a, b, count):
    import random
    if b - a < count:
        return [a, b]
    else:
        return random.sample(range(a,b+1), count)

def sum_number_list(func):
    def wrapper(a, b, count):
        numbers = func(a, b, count)
        return sum(numbers)

    return wrapper

sum_number = sum_number_list(generate_number)
total = sum_number(10, 20, 5)
print(total)


# decroator with variable arguments

def square_number(*args):
    return tuple(item * item for item in args)


def sum_numbers(func):
    def wrapper(*args, **kwargs):
        total = 0
        for item in square_number(*args, **kwargs):
            total += item

        return total

    return wrapper


squared = square_number(10,20,30)
print(squared)

sum_squared = sum_numbers(square_number)
summed = sum_squared(10, 20)
print(summed)

sum_squared = sum_numbers(square_number)
summed = sum_squared(10, 20, 30)
print(summed)
