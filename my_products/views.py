import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Substitution
from eat_better.models import Product


@require_http_methods(["POST"])
def save_substitute(request):
    """Handle ajax request to save d=the substitute."""
    if request.is_ajax():
        if request.user.is_authenticated:
            data = json.loads(request.body.decode("utf-8"))
            user = request.user
            try:
                original = Product.objects.get(id=data["original"])
                substitute = Product.objects.get(id=data["substitute"])
                Substitution.objects.create(user=user,
                                            original=original,
                                            substitute=substitute)
            except Product.DoesNotExist:
                response = {
                    "title": "Erreur",
                    "message": ("Impossible de retrouver "
                                "les produits à sauvegarder.")}
            else:
                response = {
                    "title": "Succès",
                    "message": "Le produit est sauvegardé !"}
        else:
            response = {
                "title": "Non connecté",
                "message": ("Connectez-vous pour pouvoir "
                            "sauvegarder des produits")
            }
    else:
        response = {
            "title": "Erreur",
            "message": "Erreur de requête"}
    return JsonResponse(response)


@login_required
def my_products(request):
    """Render favourites products view."""
    user = request.user
    products = Substitution.objects.filter(user=user)
    context = {"products": products}
    return render(request, "my_products/my-products.html", context)
