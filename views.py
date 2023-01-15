from django.shortcuts import render
from .models import *
from .services import get_recipes_all

# Create your views here.


def index(requests, pk=1):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/index.html', ctx)


def eng(requests):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/eng.html', ctx)


def rus(requests):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/rus.html', ctx)



