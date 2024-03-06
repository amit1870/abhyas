import copy

names = ['sitaram' ,'ramanuj' ,'bharat', 'satrudhan']
values = ['sitaram' , 'urmila', 'mandavi' , 'shrutkirti']

raghuvansi = dict(zip(names, values))
print(raghuvansi)

names = ['sitaram' ,'ramanuj' ,'bharat', 'satrudhan', 'sitaram']
values = ['sitaram' , 'urmila', 'mandavi' , 'shrutkirti', 'radha']

raghuvansi = dict(zip(names, values))
print(raghuvansi) # last value will be taken for duplicate key

ragukul = {'sita' : ['ram'] , 'anuj' : ['laxman']}

# copy using copy.copy
ragukul_copy = copy.copy(ragukul)
ragukul_copy['sita'].append('raghav')
print(ragukul_copy)
print(ragukul)

# copy using dict.copy
ragukul_copy = ragukul.copy()
ragukul_copy['anuj'].append('bharat')
print(ragukul_copy)
print(ragukul)

# copy using deepcopy
ragukul_copy = copy.deepcopy(ragukul)
ragukul_copy['anuj'].append('hanuman')
print(ragukul_copy)
print(ragukul)

a = [1,2]
b = [12,20]
c = [a,b]

d = copy.copy(c)
print(d)

e = copy.deepcopy(c)
print(e)

b.append(30)

print(b)
print(d)
print(e)


names = {'amit' : [20, 'kurmi', 'male'] , 'anil' : [15, 'amit' , 'female'], 'amis' : [14, 'aklesh', 'female']}
print(names)
sorted_names = sorted(names.items(), key=lambda value : value[1][1]) # value[1][1] apply on middle element of values(kurmi, amit, aklesh)
print(sorted_names)

# dict comprehension
dict_x = {x : x + x for x in range(3)}
print(dict_x)

generator_x = (x for x in range(3))
print(generator_x, type(generator_x)) # generator


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f

a = {'ram' : 18, 'anju' :15 }
a.update({'shayam' : 23, 'ram' : 20 })
print(a)

def find_a_value(mapping,target):
    for k,v in mapping.items():
        if v == target:
            return k

found = find_a_value(a, 15 )
print(found)
found = find_a_value(a, 18 )
print(found)

def merge_dict(mapone, maptwo):
    for k,v in maptwo.items():
        mapone[k] = v


a = {'ram' : 18, 'anju' :15 }
b = {'ram' : 11, 'bharat' :15 }
merge_dict(a, b)
print(a)

def sum_value(mapone):
    return sum(mapone.values())

result = sum_value(a)
print(result)

def find_duplicate(string):
    from collections import defaultdict
    duplicates = defaultdict(int)

    for ch in string:
        duplicates[ch] += 1

    duplicates_copy = duplicates.copy()
    for k, v in duplicates_copy.items():
        if v > 1:
            del duplicates[k]

    return duplicates

sentence = "a lazy fox jump over a monkey and don"
duplicates = find_duplicate(sentence)
print(duplicates)

def remove_duplicate_words(sentence):
    from collections import defaultdict
    words_dict = defaultdict(int)

    words = sentence.split(' ')
    for word in words:
        if word.strip() != '':
            words_dict[word] += 1

    sentence = []
    for k,v in words_dict.items():
        if v == 1:
           sentence.append(k)

    return " ".join(sentence)

senetence = "raja ram sita ram sita ram bharat anju ramanuj lamman bharat hanuman satrudhan"
senetence = remove_duplicate_words(senetence)
print(senetence)


# list comprehension
numbers = [i for i in range(9,20)]
print(numbers)

numbers = [1,2,1,1,1,22,2,34,44,44,44,5,6,7,7,8,8,9,9,9,0,0,0]
subset = [numbers[i] for i in range(0,len(numbers)) if i < len(numbers) - 2 and numbers[i] == numbers[i+1] == numbers[i+2]]
print(subset)

square_even = [i if i % 2  else i**2 for i in range(1, 20)]
print(square_even)





