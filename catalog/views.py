from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} оставил/а вам следующее сообщение: {message}')
        print(f'Телефон для связи: {phone}')

        return HttpResponse(f'{name}, благодарим за обратную связь! Ваше сообщение отправлено.')

    return render(request, 'catalog/contacts.html')

