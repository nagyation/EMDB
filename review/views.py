from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from review.models import Review
from movies.models import Movie
from review.forms import ReviewForm
from registeration.models import User
from django.db import IntegrityError
from django.db import connection

class ReviewCreate(View):

    def post(self,request,*args,**kargs):
        form = ReviewForm(request.POST)
        if(form.is_valid()):
            review = form.save(commit=False)
            #review.movie = Movie.objects.get(pk=kargs['movie_pk'])
            review.movie = Movie.objects.raw("SELECT * FROM movies_movie where id = %s", [kargs['movie_pk']])[0]
            #review.created_by = User.objects.get(id=request.user.id)
            review.created_by = User.objects.raw("SELECT * FROM registeration_user where id =%s", [request.user.id])[0]
            try:
                review.save()
            except IntegrityError as e:
                #old_review = Review.objects.filter(movie=review.movie,created_by=review.created_by)[0]
                #old_review.comment = review.comment
                #old_review.rate = review.rate
                #old_review.save()
                print("Allaahu akbaar")
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE review_review SET comment = %s, rate = %s\
                                   WHERE movie_id = %s AND created_by_id = %s",
                                   [review.comment,review.rate,review.movie.id,review.created_by.id])
            return redirect("movies:movie", kargs['movie_pk'], )



# class ReviewDelete(DeleteView):
#     model = Review
#     success_url = reverse_lazy("movies:movie")

