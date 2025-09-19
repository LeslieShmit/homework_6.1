from .models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache

class ProductService:

    @staticmethod
    def get_current_category_objects(category_id):
        products = Product.objects.filter(category_id=category_id)
        return products

def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is None:
        products = Product.objects.all()
        cache.set(key, products)
    return products