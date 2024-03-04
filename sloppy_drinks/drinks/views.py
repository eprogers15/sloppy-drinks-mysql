
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from drinks.models import Drink, Image, Episode

# Create your views here.
def drink_index(request):
    page = request.GET.get('page', 1)
    all_images = Image.objects.filter(recipe=True).distinct().order_by('drink__name')
    paginator = Paginator(all_images, 6)

    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(
        request=request,
        template_name='drink_index.html',
        context={
            'images': images,
        }
    )

def drink_index_partial(request):
    if request.htmx:
        page = request.GET.get('page', 1)
        search = request.GET.get('q')

        if search:
            all_images = Image.objects.filter((Q(drink__name__icontains=search) | Q(drink__ingredients__name__icontains=search)) & Q(recipe=True)).distinct().order_by('drink__name')
        else:
            all_images = Image.objects.filter(recipe=True).distinct().order_by('drink__name')
        paginator = Paginator(all_images, 6)

        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)

        return render(
          request=request,
          template_name='drink_index_partial.html',
          context={
              'images': images,
          }
      )
    return render(request, 'drink_index_partial.html')

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