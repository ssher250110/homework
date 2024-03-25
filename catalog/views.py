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


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}, Номер телефона: {phone}, Сообщение: {message}")
    return render(request, 'catalog/contact_info.html')
