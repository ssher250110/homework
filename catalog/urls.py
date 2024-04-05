from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('catalog/create/', ProductCreateView.as_view(), name='create_product'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('contact/', ContactView.as_view(), name='contact_info'),
]
