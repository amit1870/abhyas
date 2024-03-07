import random
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
        return self._area


class Square(Shape):
    def __init__(self, height):
        super().__init__(height=height)

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


square = Square(10)
square.calculate_and_set_area()
square.calculate_and_set_perimeter()
# print(square.area)
# print(square.perimeter)

circle = Circle(10)
circle.calculate_and_set_area()
circle.calculate_and_set_perimeter()
# print(circle.area)
# print(circle.perimeter)


def minimun_change_to_draw(square):
    squroot = math.ceil(math.sqrt(sum(square)))
    squared = squroot * squroot

    side = squared / 4

    return [side] * 4



square = random.sample(range(5,30), 4)
print(square)
square = minimun_change_to_draw(square)
print(square)






