from django.shortcuts import render
from django.views.generic import TemplateView
from movies.models import Movie
from django.shortcuts import render

# Create your views here.
class HomeView(TemplateView):
	template_name = "movies/home.html"
	def get(self,request):
		latest_movies =  list(Movie.objects.order_by("production_date").values_list('movie_logo',flat=True)[:5])
		print(latest_movies)
		return render(request,self.template_name, {'latest_movies': latest_movies})

class MovieView(TemplateView):
	template_name = "movies/moviepage.html"

class BrowseView(TemplateView):
	template_name = "movies/browse.html"

