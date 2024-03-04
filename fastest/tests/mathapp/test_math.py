import pytest


def test_add(calculator):
    assert calculator.add(2,3) == 5

def test_sub(calculator):
    assert calculator.sub(2,3) == -1

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.div(2,0)

@pytest.mark.parametrize("a,b,c", [(10,20,30), (20,20,40),(1,2,3)])
def test_add_parametrize(calculator, a, b, c):
    assert calculator.add(a,b) == c

def test_add_cmd(calculator, request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    c = request.config.getoption("--c")

    a, b, c = int(a), int(b), int(c)

    assert calculator.add(a, b) == c

