from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Beer

class BeerList(generic.ListView):
    queryset = Beer.objects.all()
    template_name = "index.html"
