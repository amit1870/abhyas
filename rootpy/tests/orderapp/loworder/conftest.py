import pytest

from src.orderapp.app import Fruit

@pytest.fixture
def my_fruit():
    return Fruit('apple')

@pytest.fixture
def your_fruit():
    return Fruit('anar')


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit('grape'), Fruit('angur'), my_fruit]


@pytest.fixture(scope="session")
def fruit_basket_session():
    return [Fruit(name) for name in ['apple', 'mango', 'anar', 'angur', 'cheeku']]

