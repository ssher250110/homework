from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def contact_info(request):
    return render(request, 'contact_info.html')
