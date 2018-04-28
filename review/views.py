from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from review.models import Review
from movies.models import Movie
from review.forms import ReviewForm
from registeration.models import User
from django.db import IntegrityError

class ReviewCreate(View):

    def post(self,request,*args,**kargs):
        form = ReviewForm(request.POST)
        if(form.is_valid()):
            review = form.save(commit=False)
            review.movie = Movie.objects.get(pk=kargs['movie_pk'])
            review.created_by = User.objects.get(id=request.user.id)
            try:
                review.save()
            except IntegrityError as e:
                old_review = Review.objects.filter(movie=review.movie,created_by=review.created_by)[0]
                old_review.comment = review.comment
                old_review.rate = review.rate
                old_review.save()
            return redirect("movies:movie", kargs['movie_pk'], )



# class ReviewDelete(DeleteView):
#     model = Review
#     success_url = reverse_lazy("movies:movie")

