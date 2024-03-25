from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product_info, index, contact_info

app_name = CatalogConfig.name
urlpatterns = [
    path('catalog/<int:pk>', product_info, name='product_info'),
    path('', index, name='index'),
    path('contact', contact_info, name='contact_info'),
]
