from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView , ListView
from movies.forms import BrowseForm
from movies.models import Movie
from django.shortcuts import render , redirect


class HomeView(TemplateView):
	template_name = "movies/home.html"
	def get(self,request):
		latest_movies =  list(Movie.objects.order_by("-production_date").values_list('movie_logo',flat=True)[:5])
		return render(request,self.template_name, {'latest_movies': latest_movies})

class MovieView(ListView):
	template_name = "movies/moviepage.html"
	def get(self,request):
		movie = Movie.objects.get(id=11)
		directors = movie.director_set.all()
		writers = movie.writer_set.all()
		actors = movie.actor_set.all()
		arg= {'movie': movie , 'directors':directors , 'writers':writers , 'actors':actors}
		return render(request,self.template_name,arg)


class BrowseView(ListView):
	template_name = "movies/browse.html"
	def get(self,request):
		form = BrowseForm()
		all_movies = Movie.objects.order_by("-production_date")
		paginator = Paginator(all_movies, 9)  # Show 9 contacts per page
		page = request.GET.get('page')
		movies = paginator.get_page(page)
		arg = {'movies': movies , 'form':form}
		return render(request,self.template_name, arg)



	def post(self, request):
		form = BrowseForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['search']
			genre = form.cleaned_data['genre']
			sort = form.cleaned_data['sort']
			form = BrowseForm()
			all_movies = Movie.objects.filter(name__contains=text, genre__contains=genre).order_by(sort)
			paginator = Paginator(all_movies, 9)  # Show 9 contacts per page
			page = request.GET.get('page')
			movies = paginator.get_page(page)
			arg = {'movies': movies, 'form': form}
			return render(request, self.template_name, arg)