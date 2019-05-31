from django.urls import path

from . import views

urlpatterns = [
    path("save-usbstitute/", views.save_substitute, name="save_substitute"),
    path("", views.my_products, name="my_products")
]
