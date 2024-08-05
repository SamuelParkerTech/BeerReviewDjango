from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Beer(models.Model):
    """
    Stores a single beer post on the below details. 
    """    
    beer_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    brewery = models.CharField(max_length=200, unique=False)
    style = models.CharField(max_length=50, unique=False)
    abv = models.CharField(max_length=50,)
    notes = models.CharField(max_length=200,)
    content = models.TextField()
    rating = models.FloatField()
    image = CloudinaryField('image', default='placeholder') 
    status = models.IntegerField(choices=STATUS, default=0)
    """
    Orders posts by beer name
    """
    class Meta:
        ordering = ["beer_name"]

class Review(models.Model):
    """
    Stores/Adds a review to the beer detail post. 
    """
    beer_name = models.ForeignKey(
        Beer, on_delete=models.CASCADE, related_name="reviews") 
    review_content = models.TextField()
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")   
    models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True) 
    """ 
    Orders by date review was created, newest first, poster listed"
    """
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Review of {self.beer_name} by {self.poster}"
    """
    function updates review score
    """
    def update_beer_rating(self):
        reviews = self.beer_name.reviews.filter(approved=True)
        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / len(reviews) if reviews else null
        self.beer_name.rating = average_rating
        self.beer_name.save()