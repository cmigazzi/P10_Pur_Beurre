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
        for ptoduct in products:
            ProductRecorder(products)
        self.stdout.write("Database is up to date !")
