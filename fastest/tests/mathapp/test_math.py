import pytest

def test_calculator(calculator):
    calc = calculator(10,20)
    assert calc.add() == 30
    assert calc.sub() == -10
    assert calc.mul() == 200
    assert calc.div() == 10/20

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator(10,0).div()

@pytest.mark.parametrize("a,b,c", [(10,20,30), (20,20,40),(1,2,3)])
def test_add_parametrize(calculator, a, b, c):
    assert calculator(a,b).add() == c
    assert calculator(a,b).sub() == a - b
    assert calculator(a,b).mul() == a * b

    if b == 0:
        with pytest.raises(ZeroDivisionError):
            calculator(a,b).div()
    else:
        assert calculator(a,b).div() == a * b

@pytest.mark.skip(reason="cmd parameter not passed")
def test_add_cmd(calculator, request):
    a = request.config.getoption("--a")
    b = request.config.getoption("--b")
    c = request.config.getoption("--c")

    a, b, c = int(a), int(b), int(c)

    assert calculator.add(a, b) == c

