from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView
from movies.forms import BrowseForm
from movies.models import Movie, Director, Writer,Actor
from django.shortcuts import render, redirect
from review.models import Review
from registeration.models import User
from django.db import connection

class HomeView(TemplateView):
    template_name = "movies/home.html"

    def get(self, request):
        #latest_movies = list(Movie.objects.order_by("-production_date").values_list('movie_logo', flat=True)[:5])
        with connection.cursor() as cursor:
            cursor.execute("SELECT movie_logo  FROM movies_movie  order by -production_date ")
            latest_movies = [i[0] for i in list(cursor.fetchall())[:5]]
        print(latest_movies)
        movies_id = list(Movie.objects.order_by("-production_date").values_list('id', flat=True)[:5])
        return render(request, self.template_name, {'latest_movies': latest_movies, 'movies_id':movies_id})


class MovieView(ListView):
    template_name = "movies/moviepage.html"

    def get(self, request, *args, **kwargs):
        #movie = Movie.objects.get(id=kwargs['pk'])
        movie = Movie.objects.raw("SELECT * FROM movies_movie where id =%s",[kwargs['pk']])[0]
        #directors = movie.director_set.all()
        directors = Director.objects.raw("SELECT * FROM movies_director, movies_director_movies\
        WHERE movies_director.id = movies_director_movies.director_id AND movie_id = %s",
                                         [kwargs['pk']])
        #writers = movie.writer_set.all()
        writers = Writer.objects.raw("SELECT * FROM movies_writer, movies_writer_movies\
                WHERE movies_writer.id = movies_writer_movies.writer_id AND movie_id = %s",
                                         [kwargs['pk']])

        #actors = movie.actor_set.all()
        actors = Actor.objects.raw("SELECT * FROM movies_actor, movies_actor_movies\
                WHERE movies_actor.id = movies_actor_movies.actor_id AND movie_id = %s",
                                         [kwargs['pk']])

        #reviews = Review.objects.filter(movie=movie)
        reviews = Review.objects.raw("SELECT * FROM review_review where movie_id = %s", [kwargs['pk']])
        arg = {'movie': movie, 'directors': directors, 'writers': writers, 'actors': actors, 'reviews': reviews}
        if request.user.is_authenticated:
            #user = User.objects.get(id=request.user.id)
            user = User.objects.raw("SELECT * FROM registeration_user WHERE id = %s",[request.user.id])[0]
            #r = Review.objects.filter(movie=movie, created_by=user)
            r = Review.objects.raw("SELECT * FROM review_review where movie_id = %s AND created_by_id = %s",
                                   [movie.id,user.id])
            arg['review'] = r
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
        #all_movies = Movie.objects.filter(name__contains=search,
         #                                 genre__contains=genre).order_by(sort)
        all_movies = list(Movie.objects.raw("select * from movies_movie\
         where name like '%%" +search+ "%%' AND genre like '%%"+genre+"%%' ORDER by %s ASC",[sort]))
        paginator = Paginator(all_movies, 9)  # Show 9 contacts per page
        page = request.GET.get('page')
        if page == None:
            page = 1
        movies = paginator.get_page(page)
        arg = {'movies': movies, 'form': form}
        return render(request, self.template_name, arg)

