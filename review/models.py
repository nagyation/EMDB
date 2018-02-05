from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    rate = models.IntegerField(blank=False, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    comment = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return "Movie: " + self.movie.name + " " + \
               "User: " + self.created_by.first_name + " " +\
               "Review: " + self.comment + " " + str(self.rate)
    class Meta:
        unique_together = ('movie', 'created_by',)