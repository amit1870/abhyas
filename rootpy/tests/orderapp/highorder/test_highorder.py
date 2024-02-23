import pytest

from src.orderapp.app import Fruit

def test_basket_scope(fruit_basket):
    assert Fruit('apple').name in fruit_basket

