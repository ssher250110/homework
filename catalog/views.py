from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def contact_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}, Номер телефона: {phone}, Сообщение: {message}")
    return render(request, 'contact_info.html')
