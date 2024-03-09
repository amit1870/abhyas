import math

from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self, radius=0, height=0, width=0):
        self.radius = radius
        self.height = height
        self.width = width
        self._area = 0
        self._perimeter = 0

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, height, width=0):
        super().__init__(height=height, width=width)

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    def calculate_and_set_area(self):
        self._area = self.height * self.height

    def calculate_and_set_perimeter(self):
        self._perimeter = 4 * self.height

class Rectangle(Square):
    def __init__(self, height, width):
        super().__init__(height=height, width=width)

    def calculate_and_set_area(self):
        self._area = self.height * self.width

    def calculate_and_set_perimeter(self):
        self._perimeter = 2 * (self.height + self.width)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius=radius)

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    def calculate_and_set_area(self):
        self._area = math.pi * self.radius * self.radius

    def calculate_and_set_perimeter(self):
        self._perimeter = 2  * math.pi * self.radius



class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

