from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_info, ProductListView, ProductDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_info'),
    path('contact', contact_info, name='contact_info'),
]
