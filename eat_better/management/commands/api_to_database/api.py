"""Contains the Api class to get data from OpenFoodFacts API."""
import datetime
import re

import requests


class Api():
    """Represent the API caller."""

    def __init__(self):
        self.CATEGORIES = ["Fromages",
                           "Biscuits et gâteaux",
                           "Produits à tartiner sucrés",
                           "Petit-déjeuners",
                           "Desserts"]
        self.FIELD_NEEDED = ["product_name_fr",
                             "categories",
                             "brands",
                             "nutriments",
                             "url",
                             "nutrition_grade_fr",
                             "image_small_url",
                             "created_t"]
        self.NUTRIMENTS = ["saturated-fat_100g",
                           "fat_100g",
                           "sugars_100g",
                           "salt_100g"]

    def call(self, update=False, sort_by="unique_scnas_n", page_size=1000):
        """Request the OpenFoodFact API to get data.

        Returns:
            list -- list of dictionnary that represents a product

        """
        clean_products = []

        for category in self.CATEGORIES:
            payload = {"search_terms": f"{category}",
                       "search_tag": "category",
                       "sort_by": sort_by,
                       "page_size": page_size,
                       "json": 1}

            response = requests.get(
                            "https://fr.openfoodfacts.org/cgi/search.pl?",
                            params=payload)

            json_response = response.json()

            products = json_response["products"]

            if update is True:
                week_ago = datetime.timedelta(days=7)
                limit_date = datetime.datetime.today() - week_ago
                products = [p for p in products
                            if p["created_t"] > int(limit_date.timestamp())]

            key_error = 0
            renamed_error = 0
            n = 0
            n_else = 0
            for product in products:
                n += 1
                try:
                    for field in self.FIELD_NEEDED:
                        if product[field] in ('', None):
                            raise KeyError
                        if field == "nutriments":
                            for nutriment in self.NUTRIMENTS:
                                if product[field][nutriment] in ('', None):
                                    raise KeyError
                except KeyError:
                    key_error += 1
                else:
                    n_else += 1
                    clean_product = {
                        k: v for k, v in product.items()
                        if k in self.FIELD_NEEDED}

                    clean_nutriments = {
                        k: v for k, v in product["nutriments"].items()
                        if k in self.NUTRIMENTS}

                    clean_product["nutriments"] = clean_nutriments

                    product_renamed = self.rename_fields(clean_product,
                                                         category)
            
                    if product_renamed is False:
                        renamed_error += 1
                        continue
                    clean_products.append(product_renamed)
        return clean_products

    @staticmethod
    def rename_fields(product, category):
        product["name"] = product.pop("product_name_fr")
        product["nutriscore"] = product.pop("nutrition_grade_fr")
        product["brand"] = product.pop("brands").split(',')[0]
        product["image"] = product.pop("image_small_url")
        categories = re.split(r",", product["categories"])
        categories = [c.strip() for c in categories]
        try:
            main_category_id = categories.index(category)
        except ValueError:
            return False
        categories = categories[main_category_id:]
        product["categories"] = [c for c in enumerate(categories)]
        nutriments = product["nutriments"]
        nutriments["saturated_fat"] = nutriments.pop("saturated-fat_100g")
        nutriments["fat"] = nutriments.pop("fat_100g")
        nutriments["sugars"] = nutriments.pop("sugars_100g")
        nutriments["salt"] = nutriments.pop("salt_100g")
        product["nutriments"] = nutriments

        return product
