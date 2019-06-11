"""Contains tests for show_original view."""

import json

from django.urls import reverse


class TestShowOriginal:

    def test_ajax_success(self, client, user_for_test, 
                          django_db_populated, multiple_substitutes):
        original = {"id": 3803}
        json_data = json.dumps(original)
        json_response = client.post(reverse("show_original"),
                                    json_data,
                                    content_type="application/json",
                                    HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        response = json.loads(json_response.content)

        assert response["title"] == "Le produit original"
        assert response["name"] == "Chocolat Dessert"
        assert response["nutriscore"] == "e"
        assert response["details"] == "/details/3803"
        assert response["image"] == "https://static.openfoodfacts.org/images/products/356/007/083/0596/front_fr.14.200.jpg"
        assert response["error"] is False

    def test_user_is_not_authenticated(self, client):
        original = {"id": 3803}
        json_data = json.dumps(original)
        response = client.post(reverse("show_original"),
                               json_data,
                               content_type="application/json",
                               HTTP_X_REQUESTED_WITH="XMLHttpRequest")

        assert response.status_code == 302
        assert "login" in response.url

    def test_post_method_is_not_ajax(self, client, user_for_test, 
                                     django_db_populated,
                                     multiple_substitutes):
        original = {"id": 3803}
        json_data = json.dumps(original)
        json_response = client.post(reverse("show_original"),
                                    json_data,
                                    content_type="application/json")
        response = json.loads(json_response.content)

        assert response["title"] == "Erreur"
        assert response["message"] == "Erreur de requête"
        assert response["error"] is True
