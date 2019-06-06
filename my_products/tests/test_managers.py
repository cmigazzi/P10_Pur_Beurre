"""Contains tests for managers of my_products application."""

from eat_better.models import Product
from core.models import User
from my_products.models import Substitution


class TestSubstitutionManager:

    def test_get_all_sustitution_for_a_user(self,
                                            django_db_populated,
                                            user_for_test):
        original = Product.objects.get(id=3803)
        substitute = Product.objects.get(id=3781)
        user = User.objects.get(email="test@test.com")
        substitution = Substitution.objects.get_or_create(
                    user=user,
                    original=original,
                    substitute=substitute
                            )

        assert Substitution.substitutes.all(original, user) == substitution
