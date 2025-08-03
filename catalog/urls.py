from django.urls import path
from . import views
from catalog.apps import CatalogConfig
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)