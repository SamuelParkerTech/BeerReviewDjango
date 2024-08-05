from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Beer

#class HomePage(TemplateView):
#    """
#    Displays home page"
#    """
#    template_name = 'index.html'

class BeerList(generic.ListView):
    queryset = Beer.objects.all()
    template_name = "index.html"
