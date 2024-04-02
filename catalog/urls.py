from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product_info, contact_info, ProductListView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('catalog/<int:pk>', product_info, name='product_info'),
    path('contact', contact_info, name='contact_info'),
]
