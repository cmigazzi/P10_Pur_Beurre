"""Contains all tests for show_substitutes view."""

import pytest

from django.urls import reverse

from eat_better.models import Product


@pytest.mark.django_db
class TestShowSubstitutes:

    def test_context(self, client, user_for_test,
                     django_db_populated, multiple_substitutes):
        product_id = 3803
        response = client.get(reverse("show_substitutes",
                                      kwargs={"original_id": product_id}))
        p_1 = Product.objects.get(id=3781)
        p_2 = Product.objects.get(id=3792)
        assert p_1 in response.context["substitutes"]
        assert p_2 in response.context["substitutes"]

    def test_user_is_not_authenticated(self, client, django_db_populated):
        product_id = 3803
        response = client.get(reverse("show_substitutes",
                                      kwargs={"original_id": product_id}))
        assert response.status_code == 302
        assert "login" in response.url

    def test_original_product_is_in_context(self, client, user_for_test,
                                            django_db_populated,
                                            multiple_substitutes):
        product_id = 3803
        product = Product.objects.get(id=product_id)
        response = client.get(reverse("show_substitutes",
                                      kwargs={"original_id": product_id}))
        assert response.context["original"] == product          