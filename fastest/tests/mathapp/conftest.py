import pytest

from src.mathapp.app import Calculator
from src.mathapp.app import Square
from src.mathapp.app import Rectangle
from src.mathapp.app import Circle

@pytest.fixture
def calculator():
    def wrapper(a,b):
        return Calculator(a, b)
    return wrapper


def pytest_addoption(parser):
    parser.addoption("--a", action="store", default="10", help="operand a")
    parser.addoption("--b", action="store", default="10", help="operand b")
    parser.addoption("--c", action="store", default="00", help="operand c")
    parser.addoption("--radius", action="store", default=0, help="radius")
    parser.addoption("--height", action="store", default=0, help="square")
    parser.addoption("--width", action="store", default=0, help="rectangle")


@pytest.fixture
def getradius(request):
    radius = 10
    config_radius = int(request.config.getoption("--radius"))
    if config_radius:
        radius = config_radius
    return radius

@pytest.fixture
def getside(request):
    side = 10
    config_height = int(request.config.getoption("--height"))
    if config_height:
        side = config_height
    return side

@pytest.fixture
def square(getside):
    return Square(getside)

@pytest.fixture
def getsides(request):
    height = width = 10
    config_height = int(request.config.getoption("--height"))
    config_width = int(request.config.getoption("--width"))
    if config_height:
        height = config_height
    if config_width:
        width = config_width
    return height, width

@pytest.fixture
def rectangle(getsides):
    height, width = getsides
    return Rectangle(height, width)

@pytest.fixture
def circle(getradius):
    return Circle(getradius)

@pytest.fixture(params=[5,10,15])
def circle_fixture_param(request):
    return Circle(request.param)

@pytest.fixture(params=[5,10,15])
def circle_with_area(request):
    c = Circle(request.param)
    c.calculate_and_set_area()
    c.calculate_and_set_perimeter()
    return c, c.area, c.perimeter

# creating global scope fixture to test
# it will not work for test which are above to package
@pytest.fixture(scope="session")
def circle_gbl(getradius):
    return Circle(getradius)