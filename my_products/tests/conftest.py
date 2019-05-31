import pytest

from django.core.management import call_command


@pytest.fixture()
def user_for_test(client, django_user_model):
    login_data = {"email": "test@test.com", "password": "djangotest"}
    django_user_model.objects.create_user(**login_data)
    client.login(**login_data)


@pytest.fixture(scope='session')
def django_db_populated(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'fixtures/db.json')
