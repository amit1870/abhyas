import pytest

from src.orderapp.app import Basket

def test_fruit_in_basket(fruits_in_basket):
    assert 'apple' in fruits_in_basket

def test_fruit_in_basket_package(fruits_in_basket):
    assert 'apple' in fruits_in_basket
