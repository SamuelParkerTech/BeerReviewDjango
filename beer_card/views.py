from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views import generic
from .models import Beer
from .forms import ReviewForm
from django.contrib import messages

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
            review.review_title = review_form.cleaned_data.get('review_title')
            review.review_content = review_form.cleaned_data.get('review_content')
            review.rating = review_form.cleaned_data.get('rating')
            review.beer_name = beer  # Explicitly associate the review with the beer
            review.save()
            messages.add_message(
                request, messages.SUCCESS,  'Review has been submitted'
            )

            
            return redirect('beer_detail', slug=slug)  # Redirect to the same page after submission

    else:
        review_form = ReviewForm()

    return render(
        request,
        "beer_detail.html",
        {"beer": beer,
        "reviews": reviews,
        "reviews_count": reviews_count, 
        "review_form": review_form,},
    )