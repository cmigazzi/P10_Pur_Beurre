"""Contains tests for search view."""

import pytest

from django.urls import reverse

from eat_better.models import Product
from my_products.models import Substitution
from core.models import User

@pytest.mark.django_db
class TestSearch:

    def test_status_code(self, client, django_db_populated):
        context = {"product": "Cake aux fruits"}
        response = client.get(reverse("search"), context)
        assert response.status_code == 200

    def test_templates(self, client, django_db_populated):
        """Test search form."""
        context = {"product": "Cake aux fruits"}
        response = client.get(reverse("search"), context)
        templates = [t.name for t in response.templates]
        assert "eat_better/results.html" in templates

    def test_products_name_in_templates(self, client, django_db_populated):
        context = {"product": "Cake aux fruits"}
        response = client.get(reverse("search"), context)
        results = response.context["results"]
        content = response.content
        for product in results:
            byte_mark = bytes(f"{product.name}", 'utf-8')
            assert byte_mark in content

    def test_product_to_search(self, client, django_db_populated):
        context = {"product": "Cake aux fruits"}
        response = client.get(reverse("search"), context)
        product = response.context["product"]
        assert isinstance(product, Product)

    def test_searched_product_not_found(self, client, django_db_populated):
        context = {"product": "steack hachés"}
        response = client.get(reverse("search"), context)
        assert response.context["product"] == context["product"]

    def test_results(self, client, django_db_populated):
        context = {"product": "Cake aux fruits"}
        response = client.get(reverse("search"), context)
        assert len(response.context["results"]) != 0
        for product in response.context["results"]:
            assert isinstance(product, Product)

    def test_searched_product_is_already_healthy(self, client,
                                                 django_db_populated):
        searched_product = Product.objects.filter(nutriscore="a")[0]
        context = {"product": searched_product.name}
        response = client.get(reverse("search"), context)

        assert response.context["is_healthy"] is True

    def test_search_with_product_id(self, client, django_db_populated):
        product_id = 3803
        product = Product.objects.get(id=product_id)
        response = client.get(reverse("search_id",
                              kwargs={"id_product": product_id})
                              )

        assert response.context["product"] == product

    def test_product_saved(self, client, django_db_populated, user_for_test):
        original = Product.objects.get(id=3803)
        substitute = Product.objects.get(id=3781)
        user = User.objects.get(email="test@test.com")
        substitution, created = Substitution.objects.get_or_create(
                    user=user,
                    original=original,
                    substitute=substitute
                            )
        response = client.get(reverse("search"))

        assert substitution in response.context["products_saved"]

