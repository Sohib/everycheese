import pytest

# connect tests to database
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

from ..models import Cheese


def test__str():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

