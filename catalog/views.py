from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['description'] = 'Auto parts'
        return context


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'title': 'Page product',
    }
    return render(request, 'catalog/product_info.html', context)


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}, Номер телефона: {phone}, Сообщение: {message}")
    return render(request, 'catalog/contact_info.html')
