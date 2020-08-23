import pytest

from pytest_django.asserts import assertContains
from django.urls import reverse
from .factories import CheeseFactory, cheese
from ..models import Cheese
from ..views import (CheeseListView, CheeseDetailView)
from everycheese.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_good_cheese_list_view_expanded(rf):
    url = reverse("cheeses:list")

    request = rf.get(url)

    callable_obj = CheeseListView.as_view()

    response = callable_obj(request)

    assertContains(response, "Cheese List")


def test_good_cheese_detail_view(rf, cheese):
    url = reverse('cheeses:detail', kwargs={'slug': cheese.slug})

    request = rf.get(url)

    callable_obj = CheeseDetailView.as_view()

    response = callable_obj(request, slug=cheese.slug)

    assertContains(response, cheese.name)


def test_good_cheese_create_view(client, user):
    client.force_login(user)

    url = reverse("cheeses:add")

    response = client.get(url)

    assert response.status_code == 200


def test_cheese_list_contains_2_cheeses(rf):
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()

    request = rf.get(reverse("cheeses:list"))

    callable_obj = CheeseListView.as_view()

    response = callable_obj(request)

    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)


def test_detail_cheese_data(rf):
    cheese = CheeseFactory()

    url = reverse('cheeses:detail', kwargs={'slug': cheese.slug})

    request = rf.get(url)

    callable_obj = CheeseDetailView.as_view()

    response = callable_obj(request, slug=cheese.slug)

    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)


def test_cheese_create_view(client, user):
    client.force_login(user)

    form = {
        "name": "Paski Sir",
        "description": "A salty hard cheese",
        "firmness": Cheese.Firmness.HARD
    }

    url = reverse("cheeses:add")

    client.post(url, form)

    cheese: Cheese = Cheese.objects.get(name=form["name"])

    assert cheese.description == form["description"]
    assert cheese.firmness == form["firmness"]
    assert cheese.creator == user


def test_good_cheese_update_view(client, user, cheese):
    url = reverse("cheeses:update", kwargs={"slug": cheese.slug})

    client.force_login(user)
    response = client.get(url)

    assertContains(response, "Update Cheese")


def test_cheese_update(client, user, cheese):
    client.force_login(user)

    form_data = {
        "name": cheese.name,
        "description": "Somthing new",
        "firmness": cheese.firmness
    }
    url = reverse("cheeses:update", kwargs={"slug": cheese.slug})
    res = client.post(url, form_data)

    cheese.refresh_from_db()
    assert cheese.description == form_data["description"]