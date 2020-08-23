from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from everycheese.cheeses.models import Cheese


class CheeseListView(ListView):
    model = Cheese
