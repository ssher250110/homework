from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import base

app_name = CatalogConfig.name
urlpatterns = [
    path('', base, name='base'),
]
