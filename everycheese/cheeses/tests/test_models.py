import pytest

# connect tests to database
pytestmark = pytest.mark.django_db

from ..models import Cheese


def test__str():
    cheese = Cheese.objects.create(
        name="Hallomi", description="lorem", firmness=Cheese.Firmness.SEMI_SOFT
    )
    assert cheese.__str__() == "Hallomi"
    assert str(cheese) == "Hallomi"

