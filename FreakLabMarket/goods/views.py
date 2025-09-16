from django.shortcuts import render

from goods.models import Products, Categories
from django.core.paginator import Paginator


def catalog(request):
    goods = Products.objects.all()
    categories = Categories.objects.all()

    paginator = Paginator(goods, 3)
    current_page = paginator.page(1)

    context = {
        'goods': current_page,
        'categories': categories,
    }
    return render(request, "goods/catalog.html", context)


def product(request, slug):
    prod = Products.objects.get(slug=slug)
    context = {
        'good': prod
    }

    return render(request, "goods/product.html", context=context)
