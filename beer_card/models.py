from django.db import models
from django.contrib.auth.models import User
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
    rating = models.IntegerField()
    image = CloudinaryField('image', default='placeholder') 
    status = models.IntegerField(choices=STATUS, default=0)