"""Contains tests for delete_substitute view."""


import json

import pytest

from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from eat_better.models import Product
from core.models import User
from my_products.models import Substitution


@pytest.mark.django_db
class TestDeleteSubstitute:

    def test_deletion(self, client, django_db_populated, user_for_test):
        original = Product.objects.get(id=3803)
        substitute = Product.objects.get(id=3781)
        user = User.objects.get(email="test@test.com")
        substitution = Substitution.objects.get_or_create(
                                user=user,
                                original=original,
                                substitute=substitute
                            )[0]

        data = {"id": substitution.id}
        json_data = json.dumps(data)
        json_response = client.post(reverse("delete_substitute"),
                                    json_data,
                                    content_type="application/json",
                                    HTTP_X_REQUESTED_WITH="XMLHttpRequest")

        with pytest.raises(ObjectDoesNotExist):
            Substitution.objects.get(id=substitution.id)

        response = json.loads(json_response.content)

        assert response["title"] == "Succès"

    def test_user_not_authenticated(self, client):
        product = {"original": 3803, 
                   "substitute": 3781}
        json_data = json.dumps(product)
        json_response = client.post(reverse("delete_substitute"),
                                    json_data,
                                    content_type="application/json",
                                    HTTP_X_REQUESTED_WITH="XMLHttpRequest")

        response = json.loads(json_response.content)
        assert response["title"] == "Non connecté"

    def test_without_ajax(self, client):
        product = {"original": 3803, 
                   "substitute": 3781}
        json_data = json.dumps(product)
        json_response = client.post(reverse("delete_substitute"),
                                    json_data,
                                    content_type="application/json")

        response = json.loads(json_response.content)
        assert response["title"] == "Erreur"
