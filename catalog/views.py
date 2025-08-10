from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} оставил/а вам следующее сообщение: {message}')
        print(f'Телефон для связи: {phone}')

        return HttpResponse(f'{name}, благодарим за обратную связь! Ваше сообщение отправлено.')

    return render(request, 'catalog/contacts.html')

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product' : product}
    return render(request, 'catalog/product_details.html', context)