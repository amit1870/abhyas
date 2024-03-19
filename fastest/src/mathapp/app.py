import math

from abc import abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self._side = side
        self._area = self._side * self._side
        self._perimeter = 4 * self._side

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
        self._area = math.pi * self._radius * self._radius
        self._perimeter = 2 * math.pi * self._radius

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter


class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

