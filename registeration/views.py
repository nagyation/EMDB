from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View
from registeration.forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class LoginView(TemplateView):
	template_name = "registeration/login.html"

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			validate_password(password,user=u)
			user_name = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, user_name=user_name, password=password)
			if user is not None:
				login(request, user)
				return redirect('movies:home')

		return render(request,self.template_name,  {'form': form })


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
			user = form.save()
			user_name = form.cleaned_data['username']
			password = form.cleaned_data['password']
			login(request,user )
			return redirect('movies:home')

		return render(request,self.template_name,  {'form': form })

class LogoutView(View):

	def get(self, request):
		logout(request)
		return redirect('movies:home')
