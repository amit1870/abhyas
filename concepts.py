# list comprehension
# list comprehension with if
# list comprehension with if-else

nlist = [i for i in range(1, 10)]
evenlist = [i for i in nlist if i % 2 == 0]
oddlist = [i for i in nlist if i % 2 != 0]
oddpadzero = [i if i % 2 == 0 else 0 for i in nlist]
evenpadzero = [i if i % 2 != 0 else 0 for i in nlist]
numbers = [1,2,1,1,1,22,2,34,44,44,44,5,6,7,7,8,8,9,9,9,0,0,0]
subset = [numbers[i] for i in range(0,len(numbers)) if i < len(numbers) - 2 and numbers[i] == numbers[i+1] == numbers[i+2]]

print(subset)
print(nlist)
print(evenlist)
print(oddlist)
print(oddpadzero)
print(evenpadzero)

# lambda with map, filter, reduce
from functools import reduce
eventozero = lambda x : x if x % 2 != 0 else 0
oddtozero = lambda x :  x if x % 2 == 0 else 0

oddpadzero = list(map(oddtozero, nlist))
evenpadzero = list(map(eventozero, nlist))
addnum = lambda a, b : a + b
summation = reduce(addnum, oddpadzero)
print(oddpadzero)
print(evenpadzero)
print(summation)

def gettable(n):
    table = []
    count = 1
    while count <= 10:
        table.append(n * count )
        count += 1

    return table

def getoddtable(table):
    if table[0] % 2 != 0:
        return table
    else:
        return []

def add(a,b):
    return a + b


tables = map(gettable, nlist)
tables = filter(getoddtable, tables)
summation = reduce(add, nlist)
print(summation)
for table in tables:
    print(table)

