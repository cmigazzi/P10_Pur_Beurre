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
    context = {"products": products,
               "originals": {p.original for p in products}}
    return render(request, "my_products/my-products.html", context)


@require_http_methods(["POST"])
def delete_substitute(request):
    """Handle ajax request to save d=the substitute."""
    if request.is_ajax():
        if request.user.is_authenticated:
            data = json.loads(request.body.decode("utf-8"))
            substitution = Substitution.objects.get(id=data["id"])
            substitution.delete()
            response = {"title": "Succès",
                        "message": "Le produit a bien été supprimé."}
        else:
            response = {"title": "Non connecté",
                        "message":
                            "Connectez-vous pour pouvoir gérer vos produits"}
    else:
        response = {"title": "Erreur",
                    "message": "Erreur de requête"}
    return JsonResponse(response)


@login_required
def show_substitutes(request, original_id):
    """handle ajax request to show all subtitutes saved."""
    substitutions = Substitution.objects.filter(user=request.user,
                                                original__id=original_id)
    substitutes = [p.substitute for p in substitutions]
    context = {"substitutes": substitutes}
    return render(request, "my_products/show-substitutes.html", context)
