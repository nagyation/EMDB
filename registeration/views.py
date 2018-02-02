from django.shortcuts import render
from django.views.generic import TemplateView
from registeration.forms import RegisterForm,LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate,login

# Create your views here.

class LoginView(TemplateView):
	template_name = "registeration/login.html"

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)

			else:
				messages.info(request, 'You must verify the data !')




	def get(self,request):
		form =LoginForm()
		return render(request,self.template_name,  {'form': form })



class RegisterView(TemplateView):
	template_name = "registeration/register.html"

	def get(self,request):
		form =RegisterForm()
		return render(request,self.template_name,  {'form': form })

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request,username=username,password =password )
			login(request,user )
			return render(request, self.template_name, {'form': form})

