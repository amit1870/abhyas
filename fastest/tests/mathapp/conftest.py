import pytest

from src.mathapp.app import Calculator
from src.mathapp.app import Square
from src.mathapp.app import Circle

@pytest.fixture
def square():
    def _square(side):
        return Square(side)

    return _square

@pytest.fixture
def circle():
    def _circle(radius):
        return Circle(radius)

    return _circle


@pytest.fixture
def calculator():
    return Calculator()


