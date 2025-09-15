from django.shortcuts import render

from goods.models import Products, Categories


def catalog(request):
    goods = Products.objects.all()
    categories = Categories.objects.all()

    context = {
        'goods': goods,
        'categories': categories,
    }
    return render(request, "goods/catalog.html", context)

def product(request):
    return render(request, "goods/product.html")