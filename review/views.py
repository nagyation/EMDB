from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from review.models import Review
from django.contrib.auth.decorators import login_required

@login_required
class ReviewCreate(CreateView):
    model = Review
    fields = ['comment','rate','movie']
    success_url = reverse("movies:movie")
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@login_required
class AuthorUpdate(UpdateView):
    model = Author
    fields = ['comment','rate']
    success_url = reverse("movies:movie")

@login_required
class AuthorDelete(DeleteView):
    model = Review
    success_url = reverse("movies:movie")

