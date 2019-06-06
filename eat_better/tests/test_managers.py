"""Contains tests for managers of eat_better app."""
import pytest

from eat_better.models import Product


@pytest.mark.django_db
class TestProductManager:

    def test_substitutes_number(self, django_db_populated):
        searched_product = Product.objects.get(name="Cake aux fruits")
        results = Product.search.substitutes(searched_product)

        assert len(results) <= 80

    def test_substitutes_nutriscore(self, django_db_populated):
        searched_product = Product.objects.get(name="Cake aux fruits")
        results = Product.search.substitutes(searched_product)

        for product in results:
            searched_product.nutriscore < product.nutriscore

    def test_substitutes_categories(self, django_db_populated):
        searched_product = Product.objects.get(name="Cake aux fruits")
        results = Product.search.substitutes(searched_product)

        for product in results:
            assert len([c for c in product.categories.all()
                        if c in searched_product.categories.all()]) != 0
