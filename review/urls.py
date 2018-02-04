from django.urls import path
from review.views import ReviewCreate, ReviewUpdate, ReviewDelete
from django.contrib.auth.decorators import login_required

app_name = "review"

urlpatterns = [
    path('add/', login_required(ReviewCreate.as_view()), name='review-add'),
    path('<int:pk>/', login_required(ReviewUpdate.as_view()), name='review-update'),
    path('<int:pk>/delete/', login_required(ReviewDelete.as_view()), name='review-delete'),
]

