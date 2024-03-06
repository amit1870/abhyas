# datatypes in python
# built-in data types : numeric, string, sequence, binary, mapping, boolean, set
# numeric : int, float, complex
# string  : str
# sequence : list, tuple, range
# binary   : bytes, bytearray, memoryview
# mapping  : dict
# boolean  : bool
# set      : set, frozenset

def print_type(data):
    for item in data:
        print(type(item))

int_type_a = 100
float_type_a = 100.0
complex_type_a = 100+3j

data = [int_type_a, float_type_a, complex_type_a]

print_type(data)

byte_a = bytes(3)

print(byte_a)

byte_array = bytearray(3)

print(byte_array)

set_a = set(['amit','sachin','sunil'])
print(set_a, type(set_a))

# set_a[2] = 'rajkumar' # assignment not supported in set

set_a.add("rajkumar")
print(set_a, type(set_a))

# set_a.remove('item') # will raise a KeyError as item not in set
set_a.remove('amit')
print(set_a, type(set_a))

# del set_a['suni']   # TypeError: 'set' object does not support item deletion
del set_a             # will delete the set object


frozen_set_a = frozenset(['amit','sachin','sunil'])
# frozen_set_a.remove('amit') # AttributeError: 'frozenset' object has no attribute 'remove'

# tricky question for set
set_b = {'amit', '10' ,  9, '0', 1, False, True}
# True is considered as 1 . False is considered as 0 . So 1 and True become duplicates.
print(set_b) # {False, 1, 9, '10', 'amit', '0'}


# operators : arithmetic, assignment, comparison, logical, identity, membership, bitwise

# operators : comparison

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

amit = Person('amit', 20)
amit2 = Person('amit', 20)
print(amit)
print(amit2)
result = amit == amit2
# result : False
# because == operator compare value(reference where stored). both reference are different.
print(result)

amit = 100
amit2 = 100
print(id(amit))
print(id(amit2))
result = amit == amit2
# result : True
# because == operator compare value(reference where stored). both reference are same.
print(result)

# operators : identity
# is , is not

amit = 'amit'
lalla = 'amit'
print(id(amit))
print(id(lalla))
result = amit is lalla
# result : True
# is operator compare references
print(result)

amit = 'amit'
lalla = 'lalla'
print(id(amit))
print(id(lalla))
result = amit is not lalla
# result : True
# is operator compare references
print(result)

# operators : membership
# in, not in: operator is used to test if sequence is present in object

names = ['sitaram', 'radhakrishna', 'laxminarayan']
result = 'sitaram' in names
print(result)

# operators : bitwise
# &(AND) |(OR) ^(XOR) ~(NOT) <<(LEFTSHIFT) >>(RIGHTSHIFT)

a = 10 # 1010
b = 4  # 0100
result = a & b  # bit-wise and 0000 : 0
print(result)

a = 10 # 1010
b = 2  # 0010
result = a & b  # 0010 : 2
print(result)

a = 10 # 1010
b = 2  # 0010
result = a ^ b  # 1000 : 8 # set 1 if only one bit of two is 1
print(result)

a = 10 # 1010
result = a << 2  # 101000 : 40 # shift left by two bit
print(result)

a = 10 # 1010
result = a >> 2  # 0010 : 2 # shift right by two bit(right two bit fall off)
print(result)

# operator precedence
a = 100
b = 3
result = a + ~b # 100 + ~(011) = 100 + -4 = 96
print(result)




