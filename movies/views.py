from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
	template_name = "movies/home.html"

class MovieView(TemplateView):
	template_name = "movies/moviepage.html"
	
class BrowseView(TemplateView):
	template_name = "movies/browse.html"
	