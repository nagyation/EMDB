from django.db import models
from movies.models import Movie
from registeration.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    rate = models.IntegerField(blank=False, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.CharField(max_length=10000)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
