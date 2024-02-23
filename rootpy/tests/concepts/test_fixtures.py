import pytest

from src.mathapp.app import calculator


# setup/teardown with pytest
# yield keyword is used to setup/teardown

def test_file_create_with_write(file_operation):
    with open("tmp.txt") as f:
        assert f.read() == "www.guruvarsitaram.shop"


@pytest.mark.operands('10 20')
def test_add(add):
    assert add(a, b) == 10 + 20