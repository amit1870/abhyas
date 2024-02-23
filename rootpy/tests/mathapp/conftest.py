import pytest

from src.mathapp.app import Calculator

@pytest.fixture(scope="module")
def calc():
    return Calculator(2,4)


@pytest.fixture(scope="module")
def custom_calc():
    def _calc(a, b):
        return Calculator(a, b)

    return _calc

