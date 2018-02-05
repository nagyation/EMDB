from django.urls import path,include
from movies.views import HomeView, BrowseView, MovieView
from . import views

app_name = 'movies'
urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('home', HomeView.as_view()),
	path('browse', BrowseView.as_view(), name='browse'),
	path('movie/<int:pk>', MovieView.as_view(), name='movie'),
]