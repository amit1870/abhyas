import pytest

from src.mathapp.app import Calculator

def pytest_cmdline_main(config):
    print('pytest_cmdline_main hook', config)
    print(config.option)

def pytest_runtest_setup(item):
    print('pytest_runtest_setup hook', item)

