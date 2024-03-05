# what is OOPs concept ?
# encapsulation : encapsulating data and functionality together.
# inheritance   : inherting property and methods of parents
#               : inheritance is an is-a relationship
#               : apple is-a Fruit, car is-a vehicle, dog is-a animal
# polymorphism  : same object acting differently with scenario change

# what is class and object ?
# class  : a skelton/bluprint of for an object.
# object : an object is collection of attribute and methods.

# what is class attribute and object attribute ?
# class attribute is meaned for sharing attribute values with different objects.
# object attribute is meaned for unique values with different objects.

# what is an abstract class ?
# abstract class is an interface class which should be implemented(all) by sub/child classes.

# what is method overriding ?
# the method in the subclass overrides the method in the superclass. concept called overriding.

# what is method resolution order MRO in case of multiple inheritance ?
# method resolution is done with left most class. if found a method there it will be returned.
# otherwise it will follow order of left-to-right for MRO.

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

class SitaRam(ABC):
    def __init__(self, legs=None, hands=None, eyes=None, gender=None):
        self.legs = legs
        self.hands = hands
        self.eyes = eyes
        self.gender = gender

    @abstractmethod
    def is_blind(self):
        pass

    @abstractmethod
    def is_disabled(self):
        pass


class Manushya(SitaRam):
    def __init__(self, legs, hands, eyes, gender='PLNG'):
        super().__init__(legs, hands, eyes, gender)

    def is_blind(self):
        return self.eyes == 0

    def is_disabled(self):
        return self.legs < 2 or self.hands < 2

    def do_dharm(self):
        print("do manushya dharm as in manu smrti")

class SatRupa(SitaRam):
    def __init__(self, legs, hands, eyes, gender='SLNG'):
        super().__init__(legs, hands, eyes, gender)

    def is_blind(self):
        return self.eyes == 0

    def is_disabled(self):
        return self.legs < 2 or self.hands < 2

    def do_dharm(self):
        print("do manushya ki seva with dharm")

class Braman(Manushya, SatRupa):
    def __init__(self, name, legs, hands, eyes, gender):
        super().__init__(legs, hands, eyes, gender)
        self.name = name

    def _perform_dharm(self, gender):
        if gender == 'PLNG':
            print('do sandhya vandan and guide people')

        else:
            print('do pati ki seva')

    def do_dharm(self):
        self._perform_dharm(self.gender)

    def generate_name(self):
        return f"braman {self.name}"


class Chatriya(Manushya, SatRupa):
    def __init__(self, name, legs, hands, eyes, gender):
        super().__init__(legs, hands, eyes, gender)
        self.name = name

    def _perform_dharm(self, gender):
        if gender == 'PLNG':
            print('do rajdharm and protect braman')

        else:
            print('do pati ki seva')

    def do_dharm(self):
        self._perform_dharm(self.gender)

    def generate_name(self):
        return f"chatriya {self.name}"


class Vaishya(Manushya, SatRupa):
    def __init__(self, name, legs, hands, eyes, gender):
        super().__init__(legs, hands, eyes, gender)
        self.name = name

    def _perform_dharm(self, gender):
        if gender == 'PLNG':
            print('do vaishya dharm and help raj dharm')

        else:
            print('do pati ki seva')

    def do_dharm(self):
        self._perform_dharm(self.gender)

    def generate_name(self):
        return f"vaishya {self.name}"


class Sudra(Manushya, SatRupa):
    def __init__(self, name, legs, hands, eyes, gender):
        super().__init__(legs, hands, eyes, gender)
        self.name = name

    def _perform_dharm(self, gender):
        if gender == 'PLNG':
            print('do sudra dharm and help vaishya dharm')
        else:
            print('do pati ki seva')

    def do_dharm(self):
        self._perform_dharm(self.gender)

    def generate_name(self):
        return f"sudra {self.name}"


class Kashyap(Braman):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

class Vashitha(Braman):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

class Raguvans(Chatriya):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

class Maurya(Chatriya):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

class Kurmi(Vaishya):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

    def _perform_dharm(self, gender):
        if gender == 'PLNG':
            print('do kheti with bailo ki dekhbhal ke sath and help vaishya samaj')
        else:
            print('do pati ki seva')

    def do_dharm(self):
        self._perform_dharm(self.gender)

class Kushwaha(Vaishya):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

    def _perform_dharm(self, gender):
        if gender == 'PLNG':
            print('do beej with balo ki dekhbhal ke sath and help vaishya samaj')
        else:
            print('do pati ki seva')

    def do_dharm(self):
        self._perform_dharm(self.gender)

class Charmkar(Sudra):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

class Vanvasi(Sudra):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)


class VarnSankar(Kushwaha,Kurmi):
    def __init__(self, name, legs, eyes, hands, gender):
        super().__init__(name, legs, eyes, hands, gender)

ramanuj = Kashyap('ramanuj',2,2,2,'PLNG')
ramanand = Vashitha('ramanand',2,2,2,'PLNG')
ram = Raguvans('ram',2,2,2,'PLNG')
chandragupta = Maurya('chandragupta',2,2,2,'PLNG')
amit = Kurmi('amit',2,2,2,'PLNG')
nishad = Vanvasi('nishad',2,2,2,'PLNG')
rahul = Kushwaha('rahul',2,2,2,'PLNG')
sankar = VarnSankar('sankar',2,2,2,'PLNG')

print(ramanuj)
ramanuj.do_dharm()

print(amit)
amit.do_dharm()

print(rahul)
rahul.do_dharm()

print(sankar)
sankar.do_dharm()

