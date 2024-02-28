from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from drinks.models import Drink, Image, Episode

# Create your views here.
def drink_index(request):
    all_images = Image.objects.filter(recipe=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(all_images, 6)

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    
    context = {
        "images": images,
    }

    return render(request, "drink_index.html", context)

def drink_detail(request, slug):
    drink = Drink.objects.get(slug=slug)
    recipe_image = Image.objects.filter(drink=drink, recipe=True)[0]
    non_recipe_images = Image.objects.filter(drink=drink, recipe=False)
    episodes = Episode.objects.filter(drink=drink)
    context = {
        "drink": drink,
        "recipe_image": recipe_image,
        "non_recipe_images": non_recipe_images,
        "episodes": episodes,
    }
    return render(request, "drink_detail.html", context)