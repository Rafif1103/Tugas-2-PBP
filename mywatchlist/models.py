from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    is_watched = models.CharField(max_length=3)
    film_title = models.CharField(max_length=255)
    film_rating = models.FloatField()
    film_release_date = models.TextField()
    film_review = models.TextField()