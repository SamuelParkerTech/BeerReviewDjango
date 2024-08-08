from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from .models import Beer
from .forms import ReviewForm

class BeerList(generic.ListView):
    queryset = Beer.objects.all()
    template_name = "index.html"


def beer_detail(request, slug):  
    queryset = Beer.objects.filter(status=1)
    beer = get_object_or_404(queryset, slug=slug)
    reviews = beer.reviews.all().order_by("-created_on")
    reviews_count = beer.reviews.filter(approved=True).count()
    if request.method == "POST": 
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.poster = request.user
            review.beer_name = beer_name
            review.save()
    
    review_form = ReviewForm()

    return render(
        request,
        "beer_detail.html",
        {"beer": beer,
        "reviews": reviews,
        "reviews_count": reviews_count, 
        "review_form": review_form},
    )