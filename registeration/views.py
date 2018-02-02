from django.shortcuts import render
from django.views.generic import TemplateView
from registeration.forms import RegisterForm

# Create your views here.

class LoginView(TemplateView):
	template_name = "registeration/login.html"

class RegisterView(TemplateView):
	template_name = "registeration/register.html"

	def get(self,request):
		form =RegisterForm()
		return render(request,self.template_name,  {'form': form })

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			Register= form.save(commit=False)
			Register.user = request.user
			Register.save()
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']

		args = { 'form': form,'first_name':first_name,'last_name':last_name,'email':email,'password':password,'confirm_password':confirm_password}
		return render(request, self.template_name, args)



