from django.core.management.base import BaseCommand

from .api_to_database.api import Api
from .api_to_database.product_recorder import ProductRecorder


class Command(BaseCommand):
    """Represents custom command for data updating."""

    help = "Request OpenFoodFacts API and retrieve new products"

    def handle(self, *args, **kwargs):
        """Handle updatedata command."""
        self.stdout.write("Updating database...")
        products = Api().call(update=True, sort_by="created_t", page_size=50)
        n_products = 0
        for product in products:
            record = ProductRecorder(product, update=True)
            if record.is_saved is True:
                n_products += 1
        self.stdout.write(f"Database is up to date ! {n_products} added.")
