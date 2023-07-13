from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'