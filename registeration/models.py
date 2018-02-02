from django.db import models
from django.contrib.auth.models import User



class Register(models.Model):
      first_name =models.CharField(max_length=15)
      last_name = models.CharField(max_length=15)
      email = models.EmailField()
      password = models.CharField(max_length=50)
      confirm_password = models.CharField(max_length=5)
      user = models.ForeignKey(User,  on_delete=models.CASCADE)
