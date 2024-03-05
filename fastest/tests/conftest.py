import re
import pytest

from src.pyapp.app import generate_password, simple_password

def pytest_configure(config):
    config.password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&-])[A-Za-z\d@$!%*?&-]{8,}$')

def pytest_addoption(parser):
    parser.addoption("--password", action="store", default="000", help="password for test")

@pytest.fixture
def get_strong_password():
    password = generate_password(8)
    return password

@pytest.fixture
def get_simple_password():
    password = simple_password(8)
    return password

@pytest.fixture
def get_param_password(request):
    password = request.param
    return password
