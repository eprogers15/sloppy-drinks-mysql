from django.shortcuts import render
from drinks.models import Drink, Image, Episode

# Create your views here.
def drink_index(request):
    images = Image.objects.filter(recipe=True)

    context = {
        "images": images,
    }
    return render(request, "drink_index.html", context)

def drink_detail(request, slug):
    drink = Drink.objects.get(slug=slug)
    images = Image.objects.filter(drink=drink)
    episodes = Episode.objects.filter(drink=drink)
    context = {
        "drink": drink,
        "images": images,
        "episodes": episodes,
    }
    return render(request, "drink_detail.html", context)