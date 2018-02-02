from django import forms
from registeration.models import Register



class RegisterForm(forms.ModelForm):
      first_name =forms.CharField(max_length=100)
      last_name = forms.CharField(max_length=100)
      email = forms.EmailField()
      password = forms.CharField(max_length=100,widget=forms.PasswordInput)
      confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)

      class Meta:
          model= Register
          fields=('first_name','last_name','email','password','confirm_password')
