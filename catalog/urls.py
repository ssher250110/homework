from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_info, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('catalog/create/', ProductCreateView.as_view(), name='create_product'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('contact', contact_info, name='contact_info'),
]
