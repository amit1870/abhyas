import pytest

from src.mathapp.app import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def pytest_addoption(parser):
    parser.addoption("--a", action="store", default="10", help="operand a")
    parser.addoption("--b", action="store", default="10", help="operand b")
    parser.addoption("--c", action="store", default="00", help="operand c")


