# one-line functions : anonymous function : lambda function
from functools import reduce

numbers = list(range(1,10))
print(numbers)

odds_squared = map(lambda x: x ** 2 if x % 2 else x , numbers )
print(tuple(odds_squared))


squared_only = filter(lambda x: True if x % 2 else False , numbers )
print(tuple(squared_only))

summation = reduce(lambda x, y : x + y , numbers)
print(summation)


# arguments during defintion : positional, default, arbitrary positional, arbitrary keyword
#                            : def function(pos_a, pos_b, age=20, *args, **kwargs)
# Default values are evaluated only once at the point of the function definition in the defining scope.
# So, it makes a difference when we pass mutable objects like a list or dictionary as default values.

def test_arguments(pos_a, pos_b, age=20, *args, **kwargs):
    print(f"pos_a : {pos_a}")
    print(f"pos_b : {pos_b}")

    print(f"default : {age}")
    print(f"args : {args}")
    print(f"kwargs : {kwargs}")

def access_args_and_keyword_arugment(pos_a, pos_b, age=20, *args, **kwargs):
    args_tuple = args
    keyword_dict = kwargs

    one, two, _ = args_tuple

    print(one, two)

    for key, value in keyword_dict.items():
        print(f"{key} with {value}")


pos_a = 10
pos_b = 20
age = 30
a,b,c = 100, 200, 300
value = 'amit'

# test_arguments(pos_a, pos_b)
# pos_a : 10 pos_b : 20 default : 20 args : () kwargs : {}

# test_arguments(pos_a, pos_b, age)
# pos_a : 10 pos_b : 20 default : 30 args : () kwargs : {}

# test_arguments(pos_a, pos_b, age, a)
# pos_a : 10 pos_b : 20 default : 30 args : (100,) kwargs : {}

# test_arguments(pos_a, pos_b, age, a, b)
# pos_a : 10 pos_b : 20 default : 30 args : (100, 200) kwargs : {}

test_arguments(pos_a, pos_b, age, a, b, name=value, new_name='sitaram')
# pos_a : 10 pos_b : 20 default : 30 args : (100, 200) kwargs : {'name': 'amit', 'new_name': 'sitaram'}

access_args_and_keyword_arugment(pos_a, pos_b, age, a, b, c, name=value, new_name='sitaram')

def test_mutable_position_argument(names_list, names_dict):
    names_list.append('sitaram')
    names_dict['sitaram'] = 'sitaram'

names_list = ['bharat', 'laxman']
names_dict = {'radha' : 'shyam'}
test_mutable_position_argument(names_list, names_dict)
print(names_list) # ['bharat', 'laxman', 'sitaram']
print(names_dict) # {'sitaram': 'sitaram', 'radha': 'shyam'}


def test_mutable_default_argument(names_list=[], names_dict={}):
    names_list.append('sitaram')
    names_dict['sitaram'] = 'sitaram'

names_list = ['bharat', 'laxman']
names_dict = {'radha' : 'shyam'}
test_mutable_position_argument(names_list, names_dict)
print(names_list) # ['bharat', 'laxman', 'sitaram']
print(names_dict) # {'sitaram': 'sitaram', 'radha': 'shyam'}


def test_mutable_default_argument2(names_list_new=[], names_dict_new={}):
    names_list_new.append('newsitaram')
    names_dict_new['newsitaram'] = 'newsitaram'

test_mutable_default_argument2(names_list, names_dict)
print(names_list) # ['bharat', 'laxman', 'sitaram', 'newsitaram']
print(names_dict) # {'radha': 'shyam', 'sitaram': 'sitaram', 'newsitaram': 'newsitaram'}



