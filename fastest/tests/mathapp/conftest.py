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

@pytest.fixture
def square_request(request):
    print(request)
    print(request.scope)
    print(request.node)
    return Square(10)


def pytest_addoption(parser):
    parser.addoption("--radius", action="store", help="provide radius")
    parser.addoption("--side", action="store", help="provide square side")


@pytest.fixture
def circle_radius_cmd(circle, request):
    radius = float(request.config.getoption("--radius"))
    return circle(radius)


def pytest_configure(config):
    config.mygside = float(config.getoption("--side")) or 100

@pytest.fixture
def square_side_cmd(square, pytestconfig):
    print(pytestconfig.option) # command line config Namespace() not include mygside
    print(pytestconfig.mygside) # global config access way

    side = pytestconfig.mygside
    return square(side)



