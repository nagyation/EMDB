from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from review.models import Review



class ReviewCreate(CreateView):
    model = Review
    fields = ['comment','rate','movie']
    success_url = reverse_lazy("movies:movie") # using reverse_lazy because reverse cause circular import
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ReviewUpdate(UpdateView):
    model = Review
    fields = ['comment','rate']
    success_url = reverse_lazy("movies:movie")


class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy("movies:movie")

