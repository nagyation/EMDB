from django.contrib import admin
from registeration.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User , UserAdmin)