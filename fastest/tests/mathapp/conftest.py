import pytest

from src.mathapp.app import Calculator
from src.mathapp.app import Square
from src.mathapp.app import Rectangle
from src.mathapp.app import Circle

@pytest.fixture
def calculator():
    return Calculator()

def pytest_addoption(parser):
    parser.addoption("--a", action="store", default="10", help="operand a")
    parser.addoption("--b", action="store", default="10", help="operand b")
    parser.addoption("--c", action="store", default="00", help="operand c")


@pytest.fixture
def getradius(request):
    radius = 10
    return radius

@pytest.fixture
def getside(request):
    side = 10
    return side

@pytest.fixture
def square(getside):
    return Square(getside)

@pytest.fixture
def getsides(request):
    height = width = 10
    return height, width

@pytest.fixture
def rectangle(getsides):
    height, width = getsides
    return Rectangle(height, width)

@pytest.fixture
def circle(getradius):
    return Circle(getradius)
