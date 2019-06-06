from django.db import models


class ProductQuerySet(models.QuerySet):
    """QuerySet for Product model."""
    def results(self, searched_product):
        """Search substitutes and return a list of 80 products max."""
        results = []
        for hierarchy in searched_product.hierarchy_set.all():
            pre_results = self.filter(
                            nutriscore__lt=searched_product.nutriscore,
                            categories__name=hierarchy.category) \
                            .order_by("nutriscore")

            if len(results) == 0 and len(pre_results) != 0:
                results = pre_results
                if len(results) > 80:
                    break

            elif len(results) + len(pre_results) > 80:
                results.union(pre_results)
                break

            elif len(results) != 0:
                results.union(pre_results)
        return results


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def substitutes(self, searched_product):
        return self.get_queryset().results(searched_product)
