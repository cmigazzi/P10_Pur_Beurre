from django.urls import path

from . import views

urlpatterns = [
    path("save-substitute/", views.save_substitute, name="save_substitute"),
    path("delete-substitute/",
         views.delete_substitute,
         name="delete_substitute"),
    path("", views.my_products, name="my_products")
]
