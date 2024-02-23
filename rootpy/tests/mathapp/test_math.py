import pytest

from src.mathapp.app import Calculator

calculator = Calculator(4, 2)

def test_add(calc):
    assert calc.add() == 6


def test_divide_by_zero(calc):
    calc.b = 0
    with pytest.raises(ZeroDivisionError):
        calc.div()

# advanced calculator testing with dynamic fixture

def test_add_advance(custom_calc):
    assert custom_calc(10,20).add() == 30
