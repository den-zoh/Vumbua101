from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff']


admin.site.register(CustomUser, UserAdmin)
