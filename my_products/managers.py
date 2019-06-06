from django.db import models


class SubstituteQuerySet(models.QuerySet):

    def get_substitutes_by_user(self, original, user):
        return self.filter(user=user, original=original)


class SubstitutionManager(models.Manager):

    def get_queryset(self):
        return SubstituteQuerySet(self.model, using=self._db)

    def all(self, original, user):
        return self.get_queryset().get_substitutes_by_user(original, user)
