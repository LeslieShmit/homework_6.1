from itertools import product

from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Delete all data from database and add test data from fixture'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog_test_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
