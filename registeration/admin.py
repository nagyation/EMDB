from django.contrib import admin
from registeration.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User , UserAdmin)
#please try to make this resposive for all the devices
