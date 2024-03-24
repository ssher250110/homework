from django.shortcuts import render

from catalog.models import Product


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'title': 'Page product',
    }
    return render(request, 'catalog/product_info.html', context)


def index(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list,
        'title': 'Main page',
        'description': 'Auto parts'
    }
    return render(request, 'catalog/index.html', context)
