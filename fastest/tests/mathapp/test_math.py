import math
import pytest

@pytest.mark.parametrize("a,b,c", [(10,20,30), (-10,10,0), (-10,-10,-20)])
def test_caculator_add(calculator, a, b, c):
    assert calculator.add(a, b) == c

@pytest.mark.parametrize("a,b", [(10,20), (-10,10), (-10,-10)])
def test_caculator_sub(calculator, a, b):
    assert calculator.sub(a, b) == a - b

@pytest.mark.parametrize("a,b,c", [(10,2, 20), (-10,2,-20)])
def test_caculator_mul(calculator, a, b, c):
    assert calculator.mul(a, b) == c

@pytest.mark.parametrize("a,b", [(10,2), (-10,2)])
def test_caculator_div(calculator, a, b):
    assert calculator.div(a, b) == a / b

def test_square(square):
    assert square(10).area == 100
    assert square(10).perimeter == 4 * 10
    assert square(11).area == 121
    assert square(11).perimeter == 4 * 11


def test_circle(circle):
    assert circle(5).area == math.pi * 5 * 5
    assert circle(5).perimeter == 2 * math.pi * 5
    assert circle(10).area == math.pi * 10 * 10
    assert circle(10).perimeter == 2 * math.pi * 10

