import json

from django.shortcuts import render
from django.http import JsonResponse

from .forms import SearchForm
from .models import Product


def index(request):
    """Returns view for index url."""
    if request.method == "POST":
        term = json.loads(request.body.decode("utf-8"))["term"].lower()
        products = Product.objects.filter(name__istartswith=term).distinct()[:5]
        data = [{"name": p.name} for p in products]
        return JsonResponse(data, safe=False)

    searched_form = SearchForm()
    context = {"search_form": searched_form}
    return render(request, "index.html", context)


def legals(request):
    """Returns view for legals url."""
    return render(request, "mentions-legales.html")


def search(request):
    """Returns view for search url."""
    try:
        searched_product = Product.objects.filter(
                    name=request.GET.get("product"))[0]
        results = []
        for hierarchy in searched_product.hierarchy_set.all():
            pre_results = Product.objects.filter(
                            nutriscore__lt=searched_product.nutriscore,
                            categories__name=hierarchy.category)

            if len(results) == 0 and len(pre_results) != 0:
                results = pre_results
                if len(results) > 80:
                    break

            elif len(results) + len(pre_results) > 80:
                results.union(pre_results)
                break

            elif len(results) != 0:
                results.union(pre_results)

    except IndexError:
        searched_product = request.GET.get("product")
        results = []

    context = {"product": searched_product,
               "results": results}
    return render(request, "results.html", context)
