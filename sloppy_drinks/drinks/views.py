from django.shortcuts import render
from drinks.models import Drink, Image

# Create your views here.
def drink_index(request):
    images = Image.objects.all()

    context = {
        "images": images,
    }
    return render(request, "drinks/drink_index.html", context)

def drink_detail(request, slug):
    drink = Drink.objects.get(slug=slug)
    context = {
        "drink": drink
    }
    return render(request, "drinks/drink_detail.html", context)