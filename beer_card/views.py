from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from .models import Beer

class BeerList(generic.ListView):
    queryset = Beer.objects.all()
    template_name = "index.html"


def beer_detail(request, slug):  
    queryset = Beer.objects.filter(status=1)
    beer = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "beer_detail.html",
        {"beer": beer},
    )