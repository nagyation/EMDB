from django import forms
from django.forms import ModelForm
from registeration.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email', 'image']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(id=self.instance.id).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email


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
        validate_password(password, self.instance)
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

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

