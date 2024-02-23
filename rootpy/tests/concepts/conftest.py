import os
import pytest

from src.mathapp.app import calculator

@pytest.fixture
def file_operation():
    print("opening a temp file for write")
    with open("tmp.txt", 'w') as f:
        f.write("www.guruvarsitaram.shop")

    yield
    print("closing file and removing it...")
    os.remove("tmp.txt")



@pytest.fixture
def add(request):
    marker = request.node.get_closest_marker("operands")
    operands = marker.args[0]
    a, b = operands.split(' ')

    return int(a) + int(b)