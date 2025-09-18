from itertools import product

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Category
from .forms import ProductForm, ProductModeratorForm

from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


from .services import ProductService, get_products_from_cache


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/home.html'
    ordering = ['-created_at']
    paginate_by = 5

    def get_queryset(self):
        return get_products_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_details.html'

class ProductByCategoryView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/products_by_category.html'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return ProductService.get_current_category_objects(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Category.objects.get(pk=category_id)
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.change_product'):
            return ProductForm
        elif user.has_perm('can_unpublish_product'):
            return ProductModeratorForm
        else:
            raise PermissionDenied('У вас нет прав для изменения этого товара.')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user and not request.user.has_perm('catalog.delete_product'):
            raise PermissionDenied('У вас нет прав для удаления этого товара.')
        return super().dispatch(request, *args, **kwargs)


class ContactsView(LoginRequiredMixin, View):
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
