from django.db import models

class Movie (models.Model):
	name = models.CharField(max_length=250)
	production_date = models.DateField()
	description = models.CharField(max_length=10000)
	rate = models.FloatField()
	trailer_url = models.CharField(max_length=1000)
	movie_logo = models.CharField(default='',max_length=1000)
	genre = models.CharField(default='', max_length=250)


	def __str__(self):
		return self.name+' - '+ str(self.production_date)

class Actor(models.Model):
    name = models.CharField(max_length=250)
    movies = models.ManyToManyField(Movie)
    photo = models.CharField(default='',max_length=1000)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=250)
    movies = models.ManyToManyField(Movie)
    photo = models.CharField(default='',max_length=1000)

    def __str__(self):
        return self.name

class Writer(models.Model):
    name = models.CharField(max_length=250)
    movies = models.ManyToManyField(Movie)
    photo = models.CharField(default='',max_length=1000)

    def __str__(self):
        return self.name
