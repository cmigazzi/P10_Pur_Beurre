from django.urls import path

from . import views

urlpatterns = [
    path("save-substitute/", views.save_substitute, name="save_substitute"),
    path("delete-substitute/",
         views.delete_substitute,
         name="delete_substitute"),
    path("show-substitutes/<original_id>", views.show_substitutes, name="show_substitutes"),
    path("", views.my_products, name="my_products")
]
