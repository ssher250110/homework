from django.shortcuts import render

from catalog.models import Product


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_info.html', context)


def index(request):
    product_list = Product.objects.all()
    context = {
        'products': product_list,
    }
    return render(request, 'catalog/index.html', context)
