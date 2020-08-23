import factory
import factory.fuzzy
import pytest
from slugify import slugify

from ..models import Cheese
from everycheese.users.tests.factories import UserFactory


@pytest.fixture
def cheese():
    """Get new Cheese"""
    return CheeseFactory()


@pytest.fixture
def user():
    """ Get new User """
    return UserFactory()


class CheeseFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    firmness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    country_of_origin = factory.Faker('country_code')

    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Cheese
