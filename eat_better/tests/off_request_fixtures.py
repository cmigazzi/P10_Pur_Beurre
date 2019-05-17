"""Contains all the products fixtures for the tests."""
import datetime

date = datetime.datetime.today()
today = int(date.timestamp())

OFF_MOCK_RESPONSES = {
    "good product": {
        'page_size': 10,
        "products": [
            {'nutrition_grade_fr': 'e',
                'brands': 'LU,Mondelez,Granola',
                'product_name_fr': 'Granola Chocolat au Lait',
                'categories': "Snacks, Snacks sucrés,"
                              "Biscuits et gâteaux, "
                              "Biscuits, Biscuits au chocolat,"
                              "Biscuits au chocolat au lait",
                'url': "https://fr.openfoodfacts.org/produit/"
                       "3017760826174/granola-chocolat-au-lait-lu",
                'image_small_url': "https://static.openfoodfacts.org/"
                                   "images/products/301/776/082/6174/"
                                   "front_fr.5.200.jpg",
                'nutriments': {
                    'saturated-fat_100g': '13',
                    'fat_100g': '24',
                    'sugars_100g': '30',
                    'salt_100g': 1.1938},
                'stores': "Carrefour",
                'created_t': 1351419982
             }
                ]
            },
    "bad product": {
        'page_size': 10,
        "products": [
            {'nutrition_grade_fr': 'a',
             'brands': '',
             'product_name_fr': 'Granola Chocolat au Lait',
             'categories': "Snacks, Snacks sucrés, "
                           "Biscuits et gâteaux,"
                           "Biscuits, Biscuits au chocolat,"
                           "Biscuits au chocolat au lait",
             'url': "https://fr.openfoodfacts.org/produit/"
                    "3017760826174/granola-chocolat-au-lait-lu",
             'nutriments': {
                'saturated-fat_100g': '13',
                'fat_100g': '24',
                'sugars_100g': '30',
                'salt_100g': 1.1938},
             'stores': "Carrefour"
             },
            {'nutrition_grade_fr': 'b',
                'brands': 'LU,Mondelez,Granola',
                'product_name_fr': 'Granola Chocolat au Lait',
                'url': "https://fr.openfoodfacts.org/produit/"
                       "3017760826174/granola-chocolat-au-lait-lu",
                'nutriments': {
                    'saturated-fat_100g': '13',
                    'fat_100g': '24',
                    'sugars_100g': '30',
                    'salt_100g': 1.1938},
                'stores': "Carrefour"
             },
            {'nutrition_grade_fr': 'c',
                'brands': 'LU,Mondelez,Granola',
                'product_name_fr': 'Granola Chocolat au Lait',
                'categories': "Snacks, Snacks sucrés, "
                              "Biscuits et gâteaux, "
                              "Biscuits, Biscuits au chocolat, "
                              "Biscuits au chocolat au lait",
                'url': "https://fr.openfoodfacts.org/produit/"
                       "3017760826174/granola-chocolat-au-lait-lu",
                'nutriments': {
                    'saturated-fat_100g': '',
                    'fat_100g': '24',
                    'sugars_100g': '30',
                    'salt_100g': 1.1938},
                'stores': "Carrefour"
             },
            {'nutrition_grade_fr': 'd',
                'brands': 'LU,Mondelez,Granola',
                'product_name_fr': 'Granola Chocolat au Lait',
                'categories': "Snacks, Snacks sucrés, "
                              "Biscuits et gâteaux, "
                              "Biscuits, Biscuits au chocolat, "
                              "Biscuits au chocolat au lait",
                'url': "https://fr.openfoodfacts.org/produit/"
                       "3017760826174/granola-chocolat-au-lait-lu",
                'nutriments': {
                    'saturated-fat_100g': '13',
                    'fat_100g': '24',
                    'salt_100g': 1.1938},
                'stores': "Carrefour"
             }
            ]
                },
    "date": {
        'page_size': 10,
        "products": [
            {'nutrition_grade_fr': 'e',
                'brands': 'LU,Mondelez,Granola',
                'product_name_fr': "Chocolat dessert blanc",
                'categories': "Snacks, Snacks sucrés,"
                              "Biscuits et gâteaux,"
                              "Biscuits, Biscuits au chocolat,"
                              "Biscuits au chocolat au lait",
                'url': "https://fr.openfoodfacts.org/produit/"
                       "3017760826174/granola-chocolat-au-lait-lu",
                'image_small_url': "https://static.openfoodfacts.org/"
                                   "images/products/301/776/082/6174/"
                                   "front_fr.5.200.jpg",
                'nutriments': {
                    'saturated-fat_100g': '13',
                    'fat_100g': '24',
                    'sugars_100g': '30',
                    'salt_100g': 1.1938},
                'stores': "Carrefour",
                'created_t': 1552147263
             },
            {'nutrition_grade_fr': 'e',
                'brands': 'LU,Mondelez,Granola',
                'product_name_fr': 'Granola Chocolat au Lait',
                'categories': "Snacks, Snacks sucrés, "
                              "Biscuits et gâteaux, "
                              "Biscuits, Biscuits au chocolat, "
                              "Biscuits au chocolat au lait",
                'url': "https://fr.openfoodfacts.org/produit/"
                       "3017760826174/granola-chocolat-au-lait-lu",
                'image_small_url': "https://static.openfoodfacts.org/"
                                   "images/products/301/776/082/6174/"
                                   "front_fr.5.200.jpg",
                'nutriments': {
                    'saturated-fat_100g': '13',
                    'fat_100g': '24',
                    'sugars_100g': '30',
                    'salt_100g': 1.1938},
                'stores': "Carrefour",
                'created_t': today
             }
                ]
            },
}