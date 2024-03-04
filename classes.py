# what is OOPs concept ?
# encapsulation : encapsulating data and functionality together.
# inheritance   : inherting property and methods of parents
# polymorphism  : same object acting differently with scenario change

# what is class and object ?
# class  : a skelton/bluprint of for an object.
# object : an object is collection of attribute and methods.

# what is class attribute and object attribute ?
# class attribute is meaned for sharing attribute values with different objects.
# object attribute is meaned for unique values with different objects.

# what is an abstract class ?
# abstract class is an interface class which should be implemented(all) by sub/child classes.


# decorators with classes : @classmethod, @staticmethod, @abstractmethod, @property

# @abstractmethod : to declare a method as abstract method

# @classmethod : transform a method into a class method.
#              : class method receives the class as an implicit first argument(cls).
#              : C.f()/C().f()
#              : if a class method is called for a derived class,
#              : the derived class object is passed as the implied first argument.

# @staticmethod : transform a method into a static method.
#               : a static method does not receive an implicit first argument.
#               : can be called C.f()/C().f()

# @property     : used to create getter, setter, deleter, doc
#               : property(fget, fset, fdel, doc)
#               : using property decorator can avoid breaking client code



from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, legs=2, hands=2, eyes=2):
        self.legs = legs
        self.hands = hands
        self.eyes = eyes

    @abstractmethod
    def is_blind(self):
        pass

    @abstractmethod
    def is_disabled(self):
        pass



class Student(Human):
    def __init__(self, legs, hands, eyes):
        super().__init__(legs, hands, eyes)

    def is_blind(self):
        return self.eyes < 2

    def is_disabled(self):
        return self.hands < 2 or self.legs < 2

    def eye_operation(self):
        self.eyes = 2



class Parent:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def get_profession(self):
        return self.profession

class Child(Parent):
    def __init__(self, name, father):
        self.name = name
        self.father = father
        self.profession = father.profession

    def set_profession(self, profession):
        self.profession = profession

    def __eq__(self, child):
        return self.father.name == child.father.name

    @staticmethod
    def self_learning():
        return ['Python', 'Pytest', 'Linux']

father = Parent('raja dasaratha', 'kshatriya')
child = Child('sitaram', father)
print(child)
print(child.name)
print(child.father.name)
print(child.father.profession)
print(child.profession)
child.set_profession('bramhan')
print(child.profession)
print(Child.self_learning())

ram = Child('ram', father)
laxman = Child('laxman' , father)

print(ram == laxman)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, person):
        return self.name == person.name and self.age == person.age

ram = Person('ram', 18)
laxman = Person('laxman', 18)
ramanuj = Person('laxman', 18)
print(ram == laxman)
print(ramanuj == laxman)

# @property : getter, setter, deleter

class Ram:
    def __init__(self, prefix, name):
        self._name = f"{prefix}{name}"

    @property   # getter
    def name(self):
        return self._name

    @name.setter    # setter
    def name(self, name):
        words = name.split(":")
        prefix, name = words[0], words[1]
        if prefix not in ['sita', 'radha', 'janki', 'rukmani', 'laxmi']:
            print(f"{prefix} not valid for setting ram")
            return
        self._name = f"{prefix}{name}"

    @name.deleter   # deleter
    def name(self):
        self._name = 'sitaram'


sitaram = Ram('sita','ram')
print(sitaram.name)
sitaram.name = "sita:ram"
print(sitaram.name)
sitaram.name = "radha:ram"
print(sitaram.name)
del sitaram.name
print(sitaram.name)








