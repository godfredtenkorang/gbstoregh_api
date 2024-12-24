from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # You can modify the fields displayed in the admin here if needed
    list_display = ('username', 'email', 'phone')
    search_fields = ('username', 'email', 'phone')

admin.site.register(User, CustomUserAdmin)

