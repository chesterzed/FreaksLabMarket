from django.shortcuts import render
from select import select

from goods.models import Products, Categories
from django.core.paginator import Paginator


def catalog(request):
    goods = Products.objects.all()
    categories = Categories.objects.all()

    filtered_goods, applied_filters = set_filter_settings(request, goods)
    current_page = get_current_page(request, filtered_goods)

    context = {
        'goods': current_page,
        'categories': categories,
        'applied_filters': applied_filters,
    }
    return render(request, "goods/catalog.html", context)


def set_filter_settings(request, goods):
    selected_cats = request.GET.getlist('category', None)
    min_value = request.GET.get('price-from', None)
    max_value = request.GET.get('price-to', None)
    applied_filters = dict()

    if selected_cats and 'all' not in selected_cats:
        goods = goods.filter(category__slug__in=selected_cats)
    if selected_cats:
        applied_filters['selected_cats'] = selected_cats

    if min_value:
        goods = goods.filter(price__gte=min_value)
        applied_filters['min_value'] = min_value

    if max_value:
        goods = goods.filter(price__lte=max_value)
        applied_filters['max_value'] = max_value


    return goods, applied_filters



def get_current_page(request, goods):
    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 3)
    return paginator.page(page)


def product(request, slug):
    prod = Products.objects.get(slug=slug)
    context = {
        'good': prod
    }

    return render(request, "goods/product.html", context=context)
