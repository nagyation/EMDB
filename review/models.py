from django.db import models
from movies.models import Movie
from registeration.models import User

# Create your models here.

class Review(models.Model):
    rate = models.IntegerField()
    comment = models.CharField(max_length=10000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
