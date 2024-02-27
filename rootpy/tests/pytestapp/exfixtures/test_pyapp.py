import pytest

from src.mathapp.app import Calculator

def test_add_postive():
    calc = Calculator(10, 20)
    assert calc.add() == 30


def test_add_negative():
    calc = Calculator(-10, -20)
    assert calc.add() == -30
    


def test_add_left():
    calc = Calculator(10, -20)
    assert calc.add() == -10

def test_add_right():
    calc = Calculator(-10, 20)
    assert calc.add() == 10
