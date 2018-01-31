from django.urls import path
from registeration.views import LoginView, RegisterView
from . import views

app_name = 'registeration'
urlpatterns = [

	path('', LoginView.as_view(), name = 'login'),
	path('register', RegisterView.as_view(), name = 'register'),
]