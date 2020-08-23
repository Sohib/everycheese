import pytest

# connect tests to database
from .factories import CheeseFactory, cheese

pytestmark = pytest.mark.django_db

from ..models import Cheese


def test__str(cheese):
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}'
