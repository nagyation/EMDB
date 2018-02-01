from django.db import models

class Movie (models.Model):
    name = models.CharField(max_length=250)
    production_date = models.CharField(max_length=100)
    writer = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    description = models.CharField(max_length=10000)
    rate = models.CharField(max_length=100)
    trailer_url = models.CharField(max_length=1000)
    movie_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name+' - '+ self.production_date

