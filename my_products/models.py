from django.db import models

from core.models import User
from eat_better.models import Product
from .managers import SubstitutionManager


class Substitution(models.Model):
    """Define the substitution columns/attributes."""

    objects = models.Manager()
    substitutes = SubstitutionManager()

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="+")
    original = models.ForeignKey(Product, on_delete=models.CASCADE,
                                 related_name="+")
    substitute = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   related_name="+")

    def __str__(self):
        """String representation of the model."""
        return f"original: {self.original}, substitue:{self.substitute}"
