import pytest

from django.core.management import call_command
from eat_better.models import Product
from core.models import User
from my_products.models import Substitution


@pytest.fixture()
def user_for_test(client, django_user_model):
    login_data = {"email": "test@test.com", "password": "djangotest"}
    django_user_model.objects.create_user(**login_data)
    client.login(**login_data)


@pytest.fixture(scope='session')
def django_db_populated(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'fixtures/db.json')


@pytest.fixture()
def multiple_substitutes(db):
    substitutions_id = [(3803, 3781), (3803, 3792)]
    for original_id, substitute_id in substitutions_id:
        original = Product.objects.get(id=original_id)
        substitute = Product.objects.get(id=substitute_id)
        user = User.objects.get(email="test@test.com")
        Substitution.objects.get_or_create(
                                user=user,
                                original=original,
                                substitute=substitute
                            )[0]
