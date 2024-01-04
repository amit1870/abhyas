import os
import pytest


def f():
    raise SystemExit(1)

def test_f():
    with pytest.raises(SystemExit):
        f()

def inc(x):
    return x + 1

def test_inc():
    assert inc(5) == 6


'''
Beaware : when grouping tests inside classes is that each test has a unique instance of the class.
Having each test share the same class instance would be very detrimental to test isolation and would promote poor test practices.
'''
class TestClass:
    value = 90

    def test_one(self):
        self.value = 100
        assert self.value == 100


    def test_two(self):
        assert self.value == 100




@pytest.mark.parametrize("test_input,output",[([1,2,3], 6),([3,4,5], 11)])
def test_list_sum(test_input, output):
    assert sum(test_input) == output

def capital_str(c_str):
    return c_str.upper()


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