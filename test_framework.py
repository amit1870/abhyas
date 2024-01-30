'''
pyest:

    => assert used to verify test expectations
    => will run all files of form test_*.py or *_test.py
    => raises helper to assert that some code raises exception
    => -q is used for quiet reporting
    => class name should start with Test
    => test arrangement is class is good
    => sharing fixtures for only test in that class
    => applying marks at the class level and having them implicitly apply to all tests
    => caution : when grouping tests inside classes is that each test has a unique instance of the class.
    => Having each test share the same class instance would be very detrimental to test isolation and would promote poor test practices.

'''

import os
import pytest



def zero_division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise e

@pytest.mark.excepttest
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        zero_division(10, 0)


@pytest.mark.classtest
class TestClass:
    ''' TestClass for grouping test inside a class '''
    value = 90

    def test_one(self):
        self.value = 100
        assert self.value == 100


    def test_two(self):
        assert self.value == 100



@pytest.mark.paramtest
@pytest.mark.parametrize("test_input,output",[([1,2,3], 6),([3,4,5], 11)])
def test_list_sum(test_input, output):
    assert sum(test_input) == output

def capital_str(c_str):
    return c_str.upper()

@pytest.mark.paramtest
@pytest.mark.parametrize("c_str,u_str",[('amit', 'AMIT'), ('RAhUl Patel', 'RAHUL PATEL') , ('AN si', 'ANSI')])
def test_capital_str(c_str, u_str):
    assert capital_str(c_str) == u_str


@pytest.fixture
def file_fixture():
    with open("tmp.txt", 'w') as f:
        f.write("Amit")

    yield
    os.remove("tmp.txt")



def test_file_create_with_write(file_fixture):
    with open("tmp.txt") as f:
        assert f.read() == "Amit"


