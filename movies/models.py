from django.db import models

class Movie (models.Model):
	name = models.CharField(max_length=250)
	production_date = models.DateField()
	writer = models.CharField(max_length=250)
	director = models.CharField(max_length=250)
	description = models.CharField(max_length=10000)
	rate = models.FloatField()
	trailer_url = models.CharField(max_length=1000)
	movie_logo = models.CharField(max_length=1000)
	#genre = models.CharField(max_length=250)

	def __str__(self):
		return self.name+' - '+ str(self.production_date)

class Actor(models.Model):
    name= models.CharField(max_length=250)
    movies= models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
