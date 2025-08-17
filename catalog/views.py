from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Contact
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj' : page_obj}
    data_to_console = products[:5]
    for el in data_to_console:
        print(f'{el.name} - {el.created_at}')
    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} оставил/а вам следующее сообщение: {message}')
        print(f'Телефон для связи: {phone}')

        return HttpResponse(f'{name}, благодарим за обратную связь! Ваше сообщение отправлено.')

    else:
        contacts_ = Contact.objects.all()
        context = {'contacts' : contacts_}
        return render(request, 'catalog/contacts.html', context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product' : product}
    return render(request, 'catalog/product_details.html', context)