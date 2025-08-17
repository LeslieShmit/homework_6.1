from django.contrib import admin
from .models import Category, Product, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category__name','created_at', 'updated_at')
    list_filter = ('category__name',)
    search_fields = ('name', 'description',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'tin', 'address',)
    list_filter = ('country',)
    search_fields = ('country', 'tin', 'address',)
