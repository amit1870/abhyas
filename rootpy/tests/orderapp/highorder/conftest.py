import pytest

from src.orderapp.app import Basket


@pytest.fixture(scope='package')
def fruits_in_basket():
    return ['package.apple' , 'package.mango', 'package.angur', 'package.anar', 'package.grape']




