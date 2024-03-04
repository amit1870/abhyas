# decorator : allow to extend/modify a function without touching original function
# iterator  : which implements two method __iter__() and __next__().
# generator : allow to create iterator in functional style.
# generator : no need to provide __iter__ and __next__ method.


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
