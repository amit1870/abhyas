import sys
import pytest

from src.mathapp.app import calculator

def test_add():
    assert calculator.add(1,2) == 3

def test_sub():
    assert calculator.sub(1,2) == -1

def test_mul():
    assert calculator.mul(1,2) == 2

def test_div():
    assert calculator.div(1,2) == 0.5


class TestCalculator:
    def test_add(self):
        assert calculator.add(1,2) == 3

    def test_sub(self):
        assert calculator.sub(1,2) == -1


    def test_mul(self):
        assert calculator.mul(1,2) == 2


    def test_div(self):
        assert calculator.div(1,2) == 0.5


@pytest.mark.skip(reason="ignore:these tests executed..")
def test_add():
    assert calculator.add(1,2) == 3

@pytest.mark.skip(reason="ignore:these tests executed..")
def test_sub():
    assert calculator.sub(1,2) == -1

@pytest.mark.skip(reason="ignore:these tests executed..")
def test_mul():
    assert calculator.mul(1,2) == 2

@pytest.mark.skip(reason="ignore:these tests executed..")
def test_div():
    assert calculator.div(1,2) == 0.5



@pytest.mark.skip(reason="ignore:these tests executed..")
class TestCalculator:
    def test_add(self):
        assert calculator.add(1,2) == 3

    def test_sub(self):
        assert calculator.sub(1,2) == -1


    def test_mul(self):
        assert calculator.mul(1,2) == 2


    def test_div(self):
        assert calculator.div(1,2) == 0.5



@pytest.mark.parametrize('a,b', [(1,2), (2,3), (3,4)])
def test_add(a, b):
    assert calculator.add(a, b) == a + b


@pytest.mark.parametrize('a, b', [(a, b) for a, b in zip(range(10), range(20))])
def test_div(a, b):
    assert calculator.div(a, b) == a / b



@pytest.mark.filterwarnings("ignore:.*test will raise error.*:DeprecationWarning")
@pytest.mark.parametrize('a, b', [(a, b) for a, b in zip(range(10), range(20))])
def test_mod(a, b):
    assert calculator.mod(a, b) == a % b


