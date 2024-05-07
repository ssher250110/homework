from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_key(key):
    """
    Получаем ключ для кэширования записи.
    """
    redis_cache_key = 'cache'
    return f'{redis_cache_key}.{key}'


def get_products_from_cache(model):
    if not CACHE_ENABLED:
        return model.objects.all()
    key = get_key(model.__name__)
    model_data = cache.get(key)
    if model_data is not None:
        return model_data
    model_data = model.objects.all()
    cache.set(key, model_data)
    return model_data
