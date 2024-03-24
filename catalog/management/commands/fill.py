import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read():
        with open('fixtures/catalog_data.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []

        for category in Command.json_read():
            if category['model'] == "catalog.category":
                category_for_create.append(
                    Category(pk=category['pk'],
                             name=category['fields']['name']
                             )
                )
        Category.objects.bulk_create(category_for_create)

        product_for_create = []

        for product in Command.json_read():
            if product['model'] == "catalog.product":
                product_for_create.append(
                    Product(
                        name=product['fields']['name'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price']
                    )
                )

        Product.objects.bulk_create(product_for_create)
