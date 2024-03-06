# decorator : allow to extend/modify a function without touching original function
# iterator  : which implements two method __iter__() and __next__().
# generator : allow to create iterator in functional style.
# generator : no need to provide __iter__ and __next__ method.
# function  : function are first class objects and objects can assigned/returned.


def say_sitaram(func):
    def sitaram(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"sitaram {result}"

    return sitaram

@say_sitaram
def greet(name):
    return f"jay {name}"


class GetEvenIndexItem:
    def __init__(self, nlist):
        self.nlist = nlist
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.nlist):
            self.counter += 2
            return self.nlist[self.counter - 2]
        else:
            raise StopIteration


def get_even_index_item(nlist):
    counter = 0
    while counter < len(nlist):
        yield nlist[counter]
        counter += 2

nlist = [1,2,3,4,5,6,7,8,9]
evens = GetEvenIndexItem(nlist)
evens = get_even_index_item(nlist)

print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))

def add_jay_to_names(func):
    def wrapper(*args, **kwargs):
        names = func(*args, **kwargs)
        jaynames = []
        for name in names:
            jaynames.append(f"jay {name}")

        return jaynames

    return wrapper

def add_post_to_names(func):
    def wrapper(*args, **kwargs):
        names = func(*args, **kwargs)
        postnames = []
        for name in names:
            postnames.append(f"{name} ji ki")

        return postnames

    return wrapper

# decorator chaining
@add_post_to_names
@add_jay_to_names
def generate_names():
    return ['sitaram', 'radhakrishna', 'laxminarayan', 'bankebihari']

def generate_mata():
    return ['sita', 'radha', 'kaikei', 'kaushlya', 'sumitra']


generated_names = generate_names()
print(generated_names)


# function name alias
mataye = add_jay_to_names(generate_mata)
sriadd = add_post_to_names(mataye)
print(sriadd())

mataye = add_post_to_names(add_jay_to_names(generate_mata))()
print(sriadd())

def get_table(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@get_table
def table(n):
    for i in range(1,11):
        s = n * i
        print(f"{n} X {i} = {s}")


table(2)
table(3)
table(4)


generate_names = (name for name in ['sita','radha','laxmi','rukmani'])
print(generate_names)
print(next(generate_names))
print(next(generate_names))
print(next(generate_names))
print(next(generate_names))
# print(next(generate_names)) # StopIteration

names = ['sita','radha','laxmi','rukmani']

def generate_names(names):
    for name in names:
        yield name


def greet_name():
    name = next(generate_names(names))
    print(f"sri {name}")

greet_name()
greet_name()
greet_name()


class OddIndexItem:
    def __init__(self, data):
        self.data = data
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter + 1 < len(self.data):
            self.counter += 2
            return self.data[self.counter-1]

        else:
            raise StopIteration


oddindexitem = OddIndexItem(list(range(1,10)))
print(next(oddindexitem))
print(next(oddindexitem))
print(next(oddindexitem))
print(next(oddindexitem))
# print(next(oddindexitem)) # StopIteration


def get_odd_index_item(array):
    counter = -1
    print(len(array))
    while counter < len(array) - 1:
        counter += 2
        yield array[counter]
        print(counter)


import string
array = string.ascii_uppercase
print(array)
generator_odd = get_odd_index_item(array)
for item in generator_odd:
    print(item)


array_iter = iter(array)
print(next(array_iter))
print(next(array_iter))

for item in array_iter:
    print(item, end=' ')



