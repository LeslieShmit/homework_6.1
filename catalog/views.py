from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact

from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/home.html'
    ordering = ['-created_at']
    paginate_by = 5


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/blog_form.html'
    fields = ['name', 'description', 'image', 'category', 'price', ]
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/blog_details.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price', ]
    template_name = 'catalog/blog_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/blog_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactsView(View):
    def get(self, request):
        contacts_ = Contact.objects.all()
        context = {'contacts': contacts_}
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} оставил/а вам следующее сообщение: {message}')
        print(f'Телефон для связи: {phone}')

        return HttpResponse(f'{name}, благодарим за обратную связь! Ваше сообщение отправлено.')
