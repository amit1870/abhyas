# decorator : allow to extend/modify a function without touching original function
#           : inner function allow to pass argument to original function
#           : returned inner function allow to take argument from outside of outer function
#           : variable binding to inner function
# iterator  : which implements two method __iter__() and __next__().
# generator : allow to create iterator in functional style.
# generator : no need to provide __iter__ and __next__ method.
# function  : function are first class objects and objects can assigned/returned.

# decorator without arguments
def add_sitaram(func):
    def append_sitaram():
        sitarams = []
        names = func()
        for name in names:
            sitarams.append(f"jay sitaram {name}")

        return sitarams

    return append_sitaram

@add_sitaram
def get_names():
    return ['amit', 'ajay', 'avinash', 'rahul', 'vivek', 'bharat', 'aman', 'bacchi', 'narayan']


sitaram_added_names = get_names()
print(sitaram_added_names)

def get_names():
    return ['amit', 'ajay', 'avinash', 'rahul', 'vivek', 'bharat', 'aman', 'bacchi', 'narayan']


add_sitaram_to_names = add_sitaram(get_names)
sitaram_added_names = add_sitaram_to_names()
print(sitaram_added_names)

# decorator with arguments

def add_radha(func):
    def wrapper(names):
        radha_names = []
        names = func(names)
        for name in names:
            radha_names.append(f"radha {name}")

        return radha_names

    return wrapper

@add_radha
def get_names(initial):
    if initial.lower() == 'a':
        return ['amit', 'anil', 'avadha', 'arun', 'ankur']
    elif initial.lower() == 'b':
        return ['bharat', 'bhuwan', 'bhumi', 'bhuvnesh','bansi']
    else:
        return ['sitaram', 'radhakrishna', 'hariom', 'narayan','ramanuj']

radha_added_names = get_names('c')
print(radha_added_names)


def get_name_by_inital(initial):
    if initial.lower() == 'a':
        return ['amit', 'anil', 'avadha', 'arun', 'ankur']
    elif initial.lower() == 'b':
        return ['bharat', 'bhuwan', 'bhumi', 'bhuvnesh','bansi']
    else:
        return ['sitaram', 'radhakrishna', 'hariom', 'narayan','ramanuj']

radha_added_name = add_radha(get_name_by_inital)
radha_added_names = radha_added_name('a')
print(radha_added_names)
radha_added_names = radha_added_name('b')
print(radha_added_names)
radha_added_names = radha_added_name('c')
print(radha_added_names)


def generate_number(a, b, n):
    import random
    if b - a <= 0:
        return [a, b]
    else:
        return random.sample(range(a,b+1), n)

def sum_number_list(func):
    def wrapper(a, b, n):
        numbers = func(a, b, n)
        print(numbers)
        return sum(numbers)

    return wrapper

sum_number = sum_number_list(generate_number)
total = sum_number(10, 20, 5)
print(total)

sum_number = sum_number_list(generate_number)
total = sum_number(10, 20, 6)
print(total)


def x(func):
    def wrapper(x):
        return 4 * func(x)

    return wrapper

@x
def func1(y):
    return y

print(func1(1)) #print 4
print(func1(2)) #print 8
print(func1(3)) #print 12

def g(a):
    return a - 10

def d(f):
    def w(x):
        z = f(x)
        return g(z)

    return w

def f(a):
    return a

a = 10
df = d(f)
dfa = df(a)
print(dfa)

b = 20
df = d(f)
dfb = df(b)
print(dfb)

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


squared = square_number(10,20, 30)
print(squared)

sum_squared = sum_numbers(square_number)
summed = sum_squared(10, 20)
print(summed)

sum_squared = sum_numbers(square_number)
summed = sum_squared(10, 20, 30)
print(summed)



