import pytest

from src.mathapp.app import Calculator

@pytest.fixture
def calculator():
    return Calculator(2,4)

@pytest.fixture(scope="module", params=[(2,3), (4,5)])
def custom_calculator(request):
    a,b = request.param
    return Calculator(a, b)

@pytest.fixture
def custom_param():
    def _calculator(a, b):
        return Calculator(a, b)

    return _calculator