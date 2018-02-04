from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.password_validation import validate_password



class RegisterForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password']

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class LoginForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username',  'password']

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

