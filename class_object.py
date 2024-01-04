'''
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made. 
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state.

@classmethod

Transform a method into a class method.
A class method receives the class as an implicit first argument, just like an instance method receives the instance.
To declare a class method, use this idiom:

class C:
    @classmethod
    def f(cls, arg1, arg2): ...

A class method can be called either on the class (such as C.f()) or on an instance (such as C().f()).
The instance is ignored except for its class.
If a class method is called for a derived class, the derived class object is passed as the implied first argument.


'''

class Nursery:

    @classmethod
    def restric_age(cls, age):
        if age > 6:
            print('Not Nursery')
        else:
            print('Nursery')


Nursery().restric_age(4)
Nursery.restric_age(20)

'''

@staticmethod
Transform a method into a static method.

A static method does not receive an implicit first argument. To declare a static method, use this idiom:

class C:
    @staticmethod
    def f(arg1, arg2, argN): ...
The @staticmethod form is a function decorator.

A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()). Moreover, they can be called as regular functions (such as f()).

'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def check_nursery(age):
        if age < 6:
            print("Nursery")

        else:
            print("Not Nursery")


Student('Bachi', 6).check_nursery(6)
Student.check_nursery(2)


class Dummy:
    dx = 10

    def __init__(self):
        print('1:',self.dx)
        # self.dx = 20
        print('2:',self.dx)

    def check_dx(self):
        print('3:',self.dx)

Dummy().check_dx()

'''
Best Practices and Optimization
When working with abstract classes in Python, it’s important to follow best practices to ensure your code is efficient and maintainable. 
Here are a few tips:

Another common error is not implementing all the abstract methods in a subclass of an abstract class.
If a subclass doesn’t provide implementations for all abstract methods of the superclass, Python will raise a TypeError when you try to create an instance of the subclass.

Use abstract classes when you want to provide a common interface for different classes.
Don’t overuse abstract classes. If a class doesn’t need to provide an interface and doesn’t have any abstract methods, 
it probably doesn’t need to be an abstract class.
Keep abstract classes small and focused. They should define a specific interface, not try to do too many things at once.
Remember that Python’s abc module is a runtime feature. 
Errors related to abstract classes won’t be caught until your code is actually running, so make sure to thoroughly test any code that uses abstract classes.
'''

from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self, legs, hands, eyes):
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

    # def is_disabled(self):
    #     return self.hands < 2 or self.legs < 2

    # def do_operation(self):
    #     if self.is_blind():
    #         self.eyes = 2
        


s1 = Student(1,2,1)
print(s1.is_blind())
# print(s1.do_operation())
print(s1.is_blind())
print(s1.is_disabled())