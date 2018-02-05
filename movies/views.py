from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from movies.forms import BrowseForm
from movies.models import Movie
from django.shortcuts import render, redirect
from review.models import Review
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = "movies/home.html"

    def get(self, request):
        latest_movies = list(Movie.objects.order_by("-production_date").values_list('movie_logo', flat=True)[:5])
        movies_id = list(Movie.objects.order_by("-production_date").values_list('id', flat=True)[:5])
        return render(request, self.template_name, {'latest_movies': latest_movies, 'movies_id':movies_id})


class MovieView(ListView):
    template_name = "movies/moviepage.html"

    def get(self, request, *args, **kwargs):
        movie = Movie.objects.get(id=kwargs['pk'])
        directors = movie.director_set.all()
        writers = movie.writer_set.all()
        actors = movie.actor_set.all()
        reviews = Review.objects.filter(movie=movie)
        arg = {'movie': movie, 'directors': directors, 'writers': writers, 'actors': actors, 'reviews': reviews}
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            r = Review.objects.filter(movie=movie, created_by=user)
            if (r):
                arg['review'] = r[0]
            print(arg)
        return render(request, self.template_name, arg)


class BrowseView(ListView):
    template_name = "movies/browse.html"

    def get(self, request):
        search = request.GET.get('search')
        if(not search):
            search = ""

        genre = request.GET.get('genre')
        if (not genre):
            genre = ""
        sort = request.GET.get('sort')
        if (not sort):
            sort = "-production_date"

        form = BrowseForm(initial={'sort':sort,'search':search,'genre':genre})
        all_movies = Movie.objects.filter(name__contains=search,
                                          genre__contains=genre).order_by(sort)
        paginator = Paginator(all_movies, 9)  # Show 9 contacts per page
        page = request.GET.get('page')
        if page == None:
            page = 1
        movies = paginator.get_page(page)
        arg = {'movies': movies, 'form': form}
        return render(request, self.template_name, arg)

