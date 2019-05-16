"""Contain tests configuration and fixtures"""
import pytest
import requests

from django.urls import reverse
from django.core.management import call_command

from .off_request_fixtures import OFF_MOCK_RESPONSES


@pytest.fixture(scope='session')
def django_db_populated(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'fixtures/db.json')


@pytest.fixture()
def index_url_get(client):
    """Create fixture for root url."""
    response = client.get(reverse("index"))
    return response


@pytest.fixture()
def legals_url_get(client):
    """Create fixture for /mentions-legales."""
    response = client.get('/mentions-legales/')
    return response


@pytest.fixture()
def good_product():
    return {'nutrition_grade_fr': 'e',
            'brands': 'LU,Mondelez,Granola',
            'product_name_fr': 'Granola Chocolat au Lait',
            'categories': "Snacks, Snacks sucrés, "
                          "Biscuits et gâteaux, "
                          "Biscuits, Biscuits au chocolat, "
                          "Biscuits au chocolat au lait",
            'url': "https://fr.openfoodfacts.org/produit/"
                   "3017760826174/granola-chocolat-au-lait-lu",
            'image_small_url': "https://static.openfoodfacts.org/images/"
                               "products/301/776/082/6174/front_fr.5.200.jpg",
            'nutriments': {
                            'saturated-fat_100g': '13',
                            'fat_100g': '24',
                            'sugars_100g': '30',
                            'salt_100g': 1.1938},
            }


@pytest.fixture()
def clean_product():
    return {'nutriscore': 'e',
            'brand': 'LU',
            'name': 'Granola Chocolat au Lait',
            'categories': [(0, "Biscuits et gâteaux"),
                           (1, "Biscuits"),
                           (2, "Biscuits au chocolat"),
                           (3, "Biscuits au chocolat au lait")],
            'url': "https://fr.openfoodfacts.org/produit/"
                   "3017760826174/granola-chocolat-au-lait-lu",
            'image': "https://static.openfoodfacts.org/images/products"
                     "/301/776/082/6174/front_fr.5.200.jpg",
            'nutriments': {
                          'saturated_fat': '13',
                          'fat': '24',
                          'sugars': '30',
                          'salt': 1.1938},
            'created_t': 1351419982
            }


@pytest.fixture()
def product_without_category():
    return {'nutrition_grade_fr': 'e',
            'brands': 'LU,Mondelez,Granola',
            'product_name_fr': 'Granola Chocolat au Lait',
            'categories': "Snacks, Snacks sucrés, "
                          "Biscuits, Biscuits au chocolat, "
                          "Biscuits au chocolat au lait",
            'url': "https://fr.openfoodfacts.org/produit/"
                   "3017760826174/granola-chocolat-au-lait-lu",
            'image_small_url': "https://static.openfoodfacts.org/images/"
                               "products/301/776/082/6174/front_fr.5.200.jpg",
            'nutriments': {
                            'saturated-fat_100g': '13',
                            'fat_100g': '24',
                            'sugars_100g': '30',
                            'salt_100g': 1.1938},
            }


@pytest.fixture(autouse=True)
def off_api_request(monkeypatch):
    """Patch the OpenFoodFacts API call."""
    def mock_request(*args, **kwargs):
        return requests.Response

    def mock_json(*args, **kwargs):
        return OFF_MOCK_RESPONSES["good product"]

    monkeypatch.setattr(requests, "get", mock_request)
    monkeypatch.setattr(requests.Response, "json", mock_json)


@pytest.fixture()
def off_api_bad_products(monkeypatch):
    """Patch the OpenFoodFacts API call."""
    def mock_request(*args, **kwargs):
        return requests.Response

    def mock_json(*args, **kwargs):
        return OFF_MOCK_RESPONSES["bad product"]
    monkeypatch.setattr(requests, "get", mock_request)
    monkeypatch.setattr(requests.Response, "json", mock_json)


@pytest.fixture()
def off_api_date(monkeypatch):
    """Patch the OpenFoodFacts API call."""
    def mock_request(*args, **kwargs):
        return requests.Response

    def mock_json(*args, **kwargs):
        return OFF_MOCK_RESPONSES["date"]
    monkeypatch.setattr(requests, "get", mock_request)
    monkeypatch.setattr(requests.Response, "json", mock_json)


@pytest.fixture()
def user_for_test(client, django_user_model):
    login_data = {"email": "test@test.com", "password": "djangotest"}
    django_user_model.objects.create_user(**login_data)
    client.login(**login_data)
