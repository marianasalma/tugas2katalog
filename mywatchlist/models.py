from django.db import models

# Create your models here.

class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.CharField(max_length=50)
    review = models.TextField()
