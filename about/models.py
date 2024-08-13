from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    about_pub = models.TextField()
    about_site = models.TextField()

    def __str__(self):
        return self.title
