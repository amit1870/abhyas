import pytest

from src.orderapp.app import Fruit

@pytest.fixture(scope="session")
def fruit_basket():
    return [Fruit(name).name for name in ['m.apple', 'm.mango', 'm.anar', 'm.angur', 'm.cheeku']]

def test_basket_scope(fruit_basket):
    assert Fruit('m.apple').name in fruit_basket

