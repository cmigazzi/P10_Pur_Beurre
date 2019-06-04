from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("search/<id_product>", views.search, name="search_id"),
    path("mentions-legales/", views.legals),
    path("details/<id_product>", views.details, name="details"),
]
