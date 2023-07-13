from django.db import models
from django.urls import reverse

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('movies_detail', kwargs={'movie_id': self.id})