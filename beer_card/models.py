from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Beer(models.Model):
    """
    Stores a single beer post on the below details.
    """
    beer_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    brewery = models.CharField(max_length=200, unique=False)
    style = models.CharField(max_length=50, unique=False)
    abv = models.CharField(max_length=50)
    notes = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["beer_name"]


class Review(models.Model):
    """
    Stores/Adds a review to the beer detail post.
    """
    beer_name = models.ForeignKey(
        Beer, on_delete=models.CASCADE, related_name="reviews"
    )
    review_title = models.CharField(max_length=50, unique=False)
    review_content = models.TextField()
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=3
    )
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Review of {self.beer_name} by {self.poster}"
