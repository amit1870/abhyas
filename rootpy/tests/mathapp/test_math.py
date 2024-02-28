import pytest

from src.mathapp.app import Calculator

def test_add(calculator):
    assert calculator.add() == 6

def test_sub(calculator):
    assert calculator.sub() == -2

def test_divide_by_zero(calculator):
    calculator.b = 0
    with pytest.raises(ZeroDivisionError):
        calculator.div()

def test_add_param(custom_calculator):
    assert custom_calculator.add() == 5

def test_add_custom_param(custom_param):
    assert custom_param(10,20).add() == 30

def test_sub_custom_param(custom_param):
    assert custom_param(10,20).sub() == 30

@pytest.mark.skip(reason="will delay test suite by 5 seconds")
def test_square(calculator):
    assert calculator.square() == 4

def test_square_monkeypatch(calculator,monkeypatch):
    def mock_return():
        return print("delay by 5 seconds done")

    monkeypatch.setattr('Calculator.delay', mock_return)
    assert calculator.square() == 4

