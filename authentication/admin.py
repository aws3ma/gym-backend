from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AuthAdminArea(admin.AdminSite):
    site_header = 'Users'

auth_site = AuthAdminArea(name='users')

admin.site.register(User,UserAdmin)