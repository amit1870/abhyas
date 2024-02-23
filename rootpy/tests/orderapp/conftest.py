import pytest

from src.orderapp.app import Basket


@pytest.fixture()
def fruits_in_basket():
    return ['apple' , 'mango', 'angur', 'anar', 'grape']




