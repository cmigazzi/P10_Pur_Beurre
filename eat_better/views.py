import json

from django.shortcuts import render
from django.http import JsonResponse, Http404

from .forms import SearchForm
from .models import Product

from my_products.models import Substitution


def index(request):
    """Return view for index url."""
    if request.method == "POST":
        term = json.loads(request.body.decode("utf-8"))["term"].lower()
        products = Product.objects.filter(name__istartswith=term)  \
                                  .distinct()
        products_names = [p.name for p in products]
        delete_duplicates = list(set(products_names))
        data = [{"name": name} for name in delete_duplicates][:5]
        return JsonResponse(data, safe=False)

    searched_form = SearchForm()
    context = {"search_form": searched_form}
    return render(request, "eat_better/index.html", context)


def legals(request):
    """Return view for legals url."""
    return render(request, "eat_better/mentions-legales.html")


def search(request, id_product=None):
    """Return view for search url."""
    try:
        if id_product is None:
            searched_product = Product.objects.filter(
                        name=request.GET.get("product"))[0]
        else:
            searched_product = Product.objects.get(id=id_product)

        if searched_product.nutriscore == "a":
            products_saved = None
            is_healthy = True
            results = []
        else:
            results = Product.search.substitutes(searched_product)
            is_healthy = False
            if request.user.is_authenticated:
                products_saved = Substitution.substitutes.all(searched_product,
                                                              request.user)
            else:
                products_saved = None

    except IndexError:
        searched_product = request.GET.get("product")
        products_saved = None
        results = []
        is_healthy = False

    context = {"product": searched_product,
               "products_saved": products_saved,
               "is_healthy": is_healthy,
               "results": results}
    return render(request, "eat_better/results.html", context)


def details(request, id_product):
    """Return view for details url."""
    try:
        product = Product.objects.get(id=id_product)
    except Product.DoesNotExist:
        raise Http404("Aucun produit trouvé.")
    else:
        context = {"product": product,
                   "nutriscore_url": f"img/nutriscore/{product.nutriscore}.png",
                   "nutriments": product.nutriments}
        return render(request, "eat_better/details.html", context)
