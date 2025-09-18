from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductByCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/', ProductByCategoryView.as_view(), name='products_by_category'),
]